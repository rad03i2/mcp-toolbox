# Security Policy

## Scope
MCP Toolbox is intentionally local and exposes deterministic text utilities. It does not read files, execute commands, open network connections, or accept credentials.

## Reporting
Please report a suspected vulnerability privately through GitHub's security reporting facilities when available. Do not include real secrets or personal data in public issues.

## Security notes
- Treat Base64 as an encoding, **not encryption**.
- MD5 and SHA-1 are available for compatibility/checksum workflows, not for password storage or security-sensitive signatures. Prefer SHA-256 or SHA-512 for integrity uses.
- Tool inputs are limited to 1,000,000 characters to reduce accidental memory abuse.
- JSON parsing is local and does not evaluate code.
- Keep the MCP SDK updated and review dependency changes before upgrading.
