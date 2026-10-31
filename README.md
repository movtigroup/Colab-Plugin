# Google Colab Tools — ZCode Plugin

یکپارچه‌سازی رسمی گوگل کولب برای ZCode: سرور MCP مرورگر-پل به‌همراه مرجع دستورات CLI برای کنترل بدون‌سر کولب.

Official Google Colab integration for ZCode: the official **colab-mcp** browser-bridge MCP server plus a **google-colab-cli** command reference for headless Colab control.

## ساختار مخزن / Repository layout

```
marketplace.json                  ← کاتالوگ پلاگین برای ZCode
colab/
├── .zcode-plugin/plugin.json     ← مانیفست پلاگین (v0.1.0)
├── .mcp.json                     ← سرور MCP رسمی colab-mcp (گوگل)
└── skills/
    ├── colab-mcp/SKILL.md        ← جفت‌سازی با نوت‌بوک Colab در مرورگر
    └── colab-cli/SKILL.md        ← کنترل بدون‌سر ران‌تایم‌های GPU/TPU
```

## نصب در ZCode / Install in ZCode

1. ZCode → **Plugin Marketplace → Add → Add Plugin Marketplace**
2. این مخزن را اضافه کنید: `https://github.com/movtigroup/colab.git`
3. **Personal → Google Colab Tools → Install**
4. ZCode را ری‌استارت کنید.

## پیش‌نیازها / Requirements

- [uv](https://docs.astral.sh/uv/) برای اجرای سرور MCP (`pip install uv`)
- حساب گوگل با دسترسی به [colab.research.google.com](https://colab.research.google.com)
- `google-colab-cli` فقط روی Linux/macOS پشتیبانی می‌شود؛ روی ویندوز داخل WSL اجرا کنید.

## استفاده / Usage

- بعد از ری‌استارت، از منوی مهارت‌ها `colab-mcp` یا `colab-cli` را انتخاب کنید.
- `colab-mcp`: کافیست بگویید «به کولب وصل شو» — مرورگر باز می‌شود، به حساب گوگل وارد شوید و نوت‌بوک به سرور محلی وصل می‌شود.
- `colab-cli`: مثال جریان کاری GPU:

```bash
colab new -s trainer --gpu A100
colab install -s trainer torch transformers
colab exec -s trainer -f train.py
colab download -s trainer checkpoints/model.bin ./model.bin
colab stop -s trainer
```

## منابع رسمی / Upstream

- https://github.com/googlecolab/colab-mcp (Apache-2.0)
- https://github.com/googlecolab/google-colab-cli (Apache-2.0)
