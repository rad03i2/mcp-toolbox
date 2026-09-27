## Summary

Describe the focused change and why it belongs in MCP Toolbox.

## Validation

- [ ] `python -m compileall -q src tests`
- [ ] `python -m unittest discover -s tests -v`
- [ ] I added or updated tests for behavior changes.

## MCP and security boundary

- [ ] Tool behavior remains narrowly scoped and validated.
- [ ] This change does not silently add filesystem, shell, network, credential, telemetry, or arbitrary-code capabilities.
- [ ] If the trust boundary changes, I explained the change and its safeguards below.

## Documentation

- [ ] User-facing behavior is reflected in `README.md` when applicable.
- [ ] Architecture changes are reflected in `docs/ARCHITECTURE.md`.
- [ ] Repository-facing artwork follows `docs/BRAND.md` when applicable.

## Notes

Add edge cases, client compatibility notes, or security implications here.
