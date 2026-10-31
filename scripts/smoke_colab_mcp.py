"""Smoke test: MCP stdio handshake against colab-mcp (git install via uv).

Launches the server with the exact command the plugin's .mcp.json uses,
performs the MCP initialize handshake and a tools/list round-trip, then
prints the tool names. The README/skills explain the pairing flow.
The pairing tool is expected pre-pairing; notebook tools appear after
the user pairs a browser Colab session.

Usage / استفاده:  python scripts/smoke_colab_mcp.py
"""
import json
import os
import subprocess
import sys
import time
import threading

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

CMD = [sys.executable, "-m", "uv", "tool", "run", "git+https://github.com/googlecolab/colab-mcp"]
INIT_TIMEOUT = 420.0   # first run builds the package from git / بار اول ساخت پکیج از گیت
LIST_TIMEOUT = 60.0

lines = []             # raw stdout lines
messages = []          # parsed JSON-RPC messages
err = []               # stderr lines


def reader(pipe, sink):
    for line in iter(pipe.readline, ""):
        sink.append(line.rstrip())


def parse_stdout():
    for line in lines:
        try:
            messages.append(json.loads(line))
        except json.JSONDecodeError:
            pass


def wait_for(msg_id, timeout):
    end = time.time() + timeout
    while time.time() < end:
        parse_stdout()
        for m in messages:
            if m.get("id") == msg_id and ("result" in m or "error" in m):
                return m
        if p.poll() is not None:
            raise SystemExit(f"server exited early: rc={p.returncode}\nSTDERR tail:\n" + "\n".join(err[-30:]))
        time.sleep(0.2)
    raise SystemExit(f"timeout waiting for response id={msg_id}\nSTDERR tail:\n" + "\n".join(err[-30:]))


p = subprocess.Popen(CMD, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                     text=True, encoding="utf-8", errors="replace")
threading.Thread(target=reader, args=(p.stdout, lines), daemon=True).start()
threading.Thread(target=reader, args=(p.stderr, err), daemon=True).start()


def send(obj):
    p.stdin.write(json.dumps(obj) + "\n")
    p.stdin.flush()


send({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {
    "protocolVersion": "2025-03-26",
    "capabilities": {},
    "clientInfo": {"name": "smoke-test", "version": "0.0.1"}}})

resp = wait_for(1, INIT_TIMEOUT)
info = resp.get("result", {}).get("serverInfo", {})
print("HANDSHAKE OK:", info.get("name"), info.get("version"))

send({"jsonrpc": "2.0", "method": "notifications/initialized"})
send({"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}})
resp = wait_for(2, LIST_TIMEOUT)
tools = resp.get("result", {}).get("tools", [])
names = [t["name"] for t in tools]
print("TOOLS:", names)
if not names:
    raise SystemExit("FAIL: no tools returned")

print("PAIRING TOOL PRESENT: " + str("open_colab_browser_connection" in names))

try:
    p.stdin.close()
    p.terminate()
    p.wait(timeout=5)
except Exception:
    pass
print("SMOKE TEST PASS" if "open_colab_browser_connection" in names
      else "SMOKE TEST: handshake OK but pairing tool missing")
