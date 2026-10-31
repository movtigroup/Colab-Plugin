# Changelog / تاریخچه‌ی تغییرات

All notable changes to this project are documented in this file.
همه‌ی تغییرات مهم این پروژه در همین فایل ثبت می‌شود.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to [Semantic Versioning](https://semver.org/).
قالب بر پایه‌ی [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) و نسخه‌بندی بر پایه‌ی [Semantic Versioning](https://semver.org/) است.

## [0.1.1] - 2026-10-31

### Added / افزوده شد

- **LICENSE** — full canonical Apache-2.0 text / متن رسمی و کامل Apache-2.0
- **NOTICE.md** — bilingual legal notice: non-affiliation with Google and upstream attribution / اطلاعیه‌ی حقوقی دوزبانه: عدم وابستگی به گوگل و ارجاع به پروژه‌های بالادستی
- **CHANGELOG.md** — this file / همین فایل
- **scripts/validate.py** — repository validator: JSON validity, manifest/name consistency, declared resources, skill frontmatter; also runs in CI / اعتبارسنج مخزن: اعتبار JSON، سازگاری مانیفست و نام، منابع اعلام‌شده، پیش‌ماده‌ی مهارت‌ها؛ در CI هم اجرا می‌شود
- **scripts/smoke_colab_mcp.py** — MCP stdio handshake smoke test against colab-mcp / تست دود هندشیک stdio با سرور colab-mcp
- **GitHub Actions workflow** validating the repository on every push and pull request / گردش‌کار GitHub Actions برای اعتبارسنجی مخزن در هر پوش و Pull Request
- Bilingual (fa/en) README with troubleshooting table and FAQ / README دوزبانه با جدول عیب‌یابی و پرسش‌های متداول

### Changed / تغییر کرد

- Plugin author set to `movtigroup`; version bumped to `0.1.1` (metadata and documentation only — no behavior change) / نویسنده‌ی پلاگین به `movtigroup` و نسخه به `0.1.1` (فقط فراداده و مستندات — بدون تغییر رفتار)

## [0.1.0] - 2026-10-31

### Added / افزوده شد

- Initial release of the `colab` plugin / انتشار اولیه‌ی پلاگین `colab`
- Official **colab-mcp** browser-bridge MCP server via `.mcp.json` (`python -m uv tool run git+https://github.com/googlecolab/colab-mcp`) / سرور رسمی colab-mcp از طریق `.mcp.json`
- `colab-mcp` skill — pairing ZCode with a browser Colab session / مهارت colab-mcp — جفت‌سازی ZCode با نوت‌بوک کولب در مرورگر
- `colab-cli` skill — headless Colab control (GPU/TPU runtimes, code execution, file transfer; Windows via WSL) / مهارت colab-cli — کنترل بدون‌سر کولب (ران‌تایم‌های GPU/TPU، اجرای کد، انتقال فایل؛ ویندوز از طریق WSL)
- ZCode marketplace catalog (`movti-colab`) / کاتالوگ مارکت‌پلیس ZCode (`movti-colab`)
