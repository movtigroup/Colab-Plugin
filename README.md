# Google Colab Tools for ZCode / ابزارهای گوگل کولب برای ZCode

![License](https://img.shields.io/badge/license-Apache--2.0-blue)
![Version](https://img.shields.io/badge/version-0.1.1-green)
![Type](https://img.shields.io/badge/ZCode-plugin-blueviolet)
![MCP](https://img.shields.io/badge/MCP-stdio-8A2BE2)

یکپارچه‌سازی حرفه‌ای گوگل کولب برای ZCode: سرور رسمی **colab-mcp** (پل مرورگر) به‌همراه مرجع کامل دستورات **google-colab-cli** برای کنترل بدون‌سر ران‌تایم‌های کولب.

A professional Google Colab integration for ZCode: the official **colab-mcp** browser-bridge MCP server plus a complete **google-colab-cli** command reference for headless control of Colab runtimes.

---

## ✨ What's inside / چه چیزهایی درون است

| Component / مؤلفه | FA | EN |
|---|---|---|
| **colab-mcp** (MCP server) | پل رسمی گوگل بین ZCode و نوت‌بوک کولبِ باز در مرورگر شما — اجرای سلول، کار با state کرنل | Google's official bridge between ZCode and a Colab notebook open in your browser — run cells, work with kernel state |
| **colab-cli** (skill) | مرجع کامل CLI رسمی گوگل برای ساخت سشن GPU/TPU، اجرای اسکریپت و انتقال فایل — بدون مرورگر | Reference for Google's official CLI to provision GPU/TPU sessions, run scripts, and transfer files — no browser needed |
| **scripts/** | ابزارهای توسعه: اعتبارسنج مخزن + تست دود سرور MCP | Dev tools: repository validator + MCP server smoke test |
| **CI** | اعتبارسنجی خودکار مخزن در هر پوش و PR | Automatic repo validation on every push and PR |

## 📁 Repository layout / ساختار مخزن

```
marketplace.json                       ← ZCode marketplace catalog / کاتالوگ مارکت‌پلیس
LICENSE                                ← Apache-2.0 / لایسنس
NOTICE.md                              ← legal notice (fa/en) / اطلاعیه حقوقی
CHANGELOG.md                           ← version history / تاریخچه نسخه‌ها
colab/
├── .zcode-plugin/plugin.json          ← plugin manifest v0.1.1 / مانیفست پلاگین
├── .mcp.json                          ← official colab-mcp server / سرور رسمی colab-mcp
└── skills/
    ├── colab-mcp/SKILL.md             ← browser pairing flow / جفت‌سازی با مرورگر
    └── colab-cli/SKILL.md             ← headless CLI reference / مرجع CLI بدون‌سر
scripts/
├── validate.py                        ← repo validator / اعتبارسنج مخزن
└── smoke_colab_mcp.py                 ← MCP handshake smoke test / تست دود سرور MCP
.github/workflows/validate.yml         ← CI / اعتبارسنجی خودکار
```

## 🚀 Install / نصب

1. ZCode → **Plugin Marketplace → Add → Add Plugin Marketplace**
2. Paste this repository / این مخزن را بچسبانید: `https://github.com/movtigroup/colab.git`
3. **Personal → Google Colab Tools → Install** → restart ZCode / ری‌استارت کنید

### Requirements / پیش‌نیازها

| Requirement | FA | EN |
|---|---|---|
| [uv](https://docs.astral.sh/uv/) | برای اجرای سرور MCP — `pip install uv` | Runs the MCP server — `pip install uv` |
| Google account | برای colab.research.google.com | For colab.research.google.com |
| WSL (Windows only) | `google-colab-cli` فقط Linux/macOS؛ روی ویندوز داخل WSL | google-colab-cli is Linux/macOS only; use WSL on Windows |

## 🧑‍💻 Usage / استفاده

- Select the `colab-mcp` or `colab-cli` skill from the composer picker, then:
  از منوی مهارت‌ها یکی را انتخاب کنید و بعد:
  - say «به کولب وصل شو» to pair with a browser Colab notebook / برای جفت‌سازی با نوت‌بوک مرورگر
  - or use the headless CLI flow / یا جریان CLI بدون‌سر:

```bash
colab new -s trainer --gpu A100
colab install -s trainer torch transformers
colab exec -s trainer -f train.py
colab download -s trainer checkpoints/model.bin ./model.bin
colab stop -s trainer
```

## 🛠 Troubleshooting / عیب‌یابی

| Symptom / علامت | Fix / راه‌حل |
|---|---|
| No Colab tools after connecting / ابزار کولب دیده نمی‌شود | Session not paired yet — call `open_colab_browser_connection`, keep the Colab tab open, sign in to Google / هنوز جفت نشده — ابزار جفت‌سازی را صدا بزنید و تب کولب را باز نگه دارید |
| Server fails to start / سرور بالا نمی‌آید | `pip install uv`, then restart ZCode / uv را نصب و ZCode را ری‌استارت کنید |
| uvx build fails / ساخت uvx شکست خورد | Add `--index https://pypi.org/simple` to `.mcp.json` args / به آرگومان‌های `.mcp.json` اضافه کنید |
| Pairing times out / جفت‌سازی تایم‌اوت شد | Call the pairing tool again (fresh 60s window) / دوباره ابزار جفت‌سازی را صدا بزنید |

## ❓ FAQ / پرسش‌های متداول

**Is this made by Google? / این محصول گوگل است؟**
No — independent integration, see [NOTICE.md](NOTICE.md). / نه — یکپارچه‌سازی مستقل است، به NOTICE مراجعه کنید.

**Where does the MCP server come from? / سرور MCP از کجا می‌آید؟**
Fetched at runtime from Google's official repo via `uv tool run` — nothing is redistributed here. / در زمان اجرا از مخزن رسمی گوگل فراخوانی می‌شود؛ چیزی بازتوزیع نمی‌شود.

**Does it cost anything? / هزینه دارد؟**
Colab free tier works; GPU/TPU and high-RAM need Colab Pro/Pro+ points. / پلن رایگان کار می‌کند؛ GPU/TPU و حافظه‌ی بالا نیاز به اشتراک Pro دارند.

## 🔧 Development / توسعه

```bash
python scripts/validate.py          # validate repo / اعتبارسنجی مخزن
python scripts/smoke_colab_mcp.py   # test MCP server / تست سرور MCP
```

CI runs the validator on every push and PR. / CI اعتبارسنج را روی هر پوش و PR اجرا می‌کند.

## 📄 License & Notice / لایسنس و اطلاعیه

Apache-2.0 — see [LICENSE](LICENSE). Legal notes in [NOTICE.md](NOTICE.md), history in [CHANGELOG.md](CHANGELOG.md).
لایسنس Apache-2.0 — اطلاعیه حقوقی در NOTICE و تاریخچه در CHANGELOG.

## 🙏 Acknowledgments / قدردانی

- [googlecolab/colab-mcp](https://github.com/googlecolab/colab-mcp) · [googlecolab/google-colab-cli](https://github.com/googlecolab/google-colab-cli) — © Google, Apache-2.0
