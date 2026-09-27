# Changelog

Notable project-facing changes are documented here.

## Unreleased

### Added

- Independent **Signal Grid** visual identity for MCP Toolbox.
- Repository hero cover and square project logo in `assets/`.
- `docs/BRAND.md` with palette, logo, typography, and visual-language guidance.
- `docs/ARCHITECTURE.md` documenting the core / FastMCP separation and trust boundaries.
- GitHub bug-report and pull-request templates.

### Changed

- Reorganized `README.md` around the actual MCP tool catalog, stdio connection model, security boundary, testing, limitations, and bilingual documentation.
- Expanded contributor guidance for new tools, tests, and trust-boundary changes.

## 1.0.0

The package currently reports version `1.0.0`.

Documented capabilities at this version:

- seven MCP tools: hashing, JSON formatting, Base64 encode/decode, text statistics, UUID v4, and UTC time;
- pure-Python reusable core;
- official Python MCP SDK / FastMCP server layer;
- local stdio execution;
- one-million-character input guard for text-processing tools;
- unit tests and cross-platform GitHub Actions configuration.
