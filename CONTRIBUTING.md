# Contributing

Thanks for your interest in improving **Google Colab Tools for ZCode**! 🎉

## How to help

There are many ways to contribute:
- 🐛 Report bugs (pairing failures, MCP server startup issues)
- 💡 Suggest features for the roadmap
- 📖 Improve documentation
- 🧪 Extend the validator or smoke test coverage
- 🔧 Polish skills' guidance for agent use

## Development setup

```bash
git clone https://github.com/movtigroup/colab.git
cd colab
python scripts/validate.py          # 15-point repo validation
python scripts/smoke_colab_mcp.py   # requires: pip install uv
```

## Pull request checklist

1. Run `python scripts/validate.py` — it must pass with zero failures
2. Update [CHANGELOG.md](CHANGELOG.md) under an **Unreleased** section
3. Bump the version in `colab/.zcode-plugin/plugin.json` **and** `marketplace.json` per SemVer
4. Keep documentation in English

## Reporting issues

Include:
- ZCode version and OS (Windows/macOS/Linux)
- Output of `python scripts/validate.py`
- For pairing problems: whether the Colab tab stayed open and whether you were signed in

## License

By contributing, you agree that your contributions are licensed under the Apache-2.0 license of this repository.
