# Contributing to MCP Toolbox

Contributions are welcome when they preserve the project's defining properties: **small scope, local operation, narrow permissions, direct tests, and clear MCP behavior**.

## Development setup

```bash
git clone https://github.com/rad03i2/mcp-toolbox.git
cd mcp-toolbox
python -m venv .venv
python -m pip install -e .
```

Run the current checks:

```bash
python -m compileall -q src tests
python -m unittest discover -s tests -v
```

## Adding or changing a tool

Prefer this sequence:

1. implement validation and behavior in `src/mcp_toolbox/core.py`;
2. add or update tests in `tests/`;
3. expose a thin typed wrapper in `src/mcp_toolbox/server.py`;
4. update the English and Arabic documentation when user-facing behavior changes;
5. explain any security or trust-boundary impact in the pull request.

## Project boundaries

Do not casually add capabilities that materially widen permissions.

In particular, additions involving the following require explicit design justification:

- arbitrary shell or process execution;
- unrestricted filesystem reads or writes;
- silent mutation of user data;
- network requests;
- credentials or secret storage;
- telemetry;
- arbitrary code evaluation.

The current project intentionally has none of these capabilities.

## Utility design

New utilities should ideally be:

- deterministic where the task itself is deterministic;
- easy to validate;
- bounded in resource use;
- useful through structured MCP arguments/results;
- independently testable without an MCP client.

If a utility introduces nondeterminism, document why.

## Pull request checklist

A focused pull request should state:

- what tool or behavior changed;
- why it belongs in this toolbox;
- how inputs are validated;
- what tests were added;
- whether the MCP trust boundary changed;
- whether README / architecture docs were updated.

## Documentation and visual identity

- Follow [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for the current component model.
- Follow [docs/BRAND.md](docs/BRAND.md) for repository-facing visuals.
- Do not describe Base64 as encryption.
- Do not advertise shell, file, browser, or network access unless the code truly implements it.

## العربية

نرحب بالمساهمات التي تحافظ على المشروع صغيرًا ومحليًا ومحدود الصلاحيات.

عند إضافة أداة جديدة، ضع المنطق والتحقق في `core.py` قدر الإمكان، ثم أضف الاختبارات، وبعدها عرّف غلاف MCP بسيطًا في `server.py`.

أي إضافة لوصول الملفات أو Shell أو الشبكة أو الأسرار تغيّر نموذج الأمان للمشروع، لذلك يجب ألا تضاف كميزة عادية دون تبرير وتصميم واختبارات واضحة.

---

Maintained by **Radwan Abd alhady Ahmed** — **رضوان عبدالهادي** — [@rad03i2](https://github.com/rad03i2)
