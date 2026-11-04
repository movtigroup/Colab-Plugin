# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Automated GitHub Release pipeline (`scripts/release/publish.sh` + `.github/workflows/release.yml`): every push to `main` that introduces a new manifest version is automatically tagged `v<version>`, validated, packaged as a plugin zip asset and published as a GitHub Release with generated notes. Tag pushes are supported too, guarded to match the manifest version.

## [0.1.1] - 2026-10-31

### Added

- **LICENSE** — full canonical Apache-2.0 text
- **NOTICE.md** — legal notice: non-affiliation with Google and upstream attribution
- **CHANGELOG.md** — this file
- **CONTRIBUTING.md** — contribution guidelines
- **scripts/validate.py** — repository validator: JSON validity, manifest/name consistency, declared resources, skill frontmatter; also runs in CI
- **scripts/smoke_colab_mcp.py** — MCP stdio handshake smoke test against colab-mcp
- **GitHub Actions workflow** validating the repository on every push and pull request
- Professional English README: badges, architecture diagram, troubleshooting, FAQ, roadmap

### Changed

- Plugin author set to `movtigroup`; version bumped to `0.1.1` (metadata and documentation only — no behavior change)

## [0.1.0] - 2026-10-31

### Added

- Initial release of the `colab` plugin
- Official **colab-mcp** browser-bridge MCP server via `.mcp.json` (`python -m uv tool run git+https://github.com/googlecolab/colab-mcp`)
- `colab-mcp` skill — pairing ZCode with a browser Colab session
- `colab-cli` skill — headless Colab control (GPU/TPU runtimes, code execution, file transfer; Windows via WSL)
- ZCode marketplace catalog (`movti-colab`)
