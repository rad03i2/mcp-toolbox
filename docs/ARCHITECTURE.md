# Architecture

MCP Toolbox is intentionally small. The architecture separates **utility behavior** from **MCP transport exposure** so that core functions can be tested and reused without starting a server.

## Components

### 1. Core utility layer

File: `src/mcp_toolbox/core.py`

Responsibilities:

- validate text input and enforce the 1,000,000-character limit;
- implement hashing;
- parse and format JSON;
- encode/decode Base64 UTF-8 text;
- calculate text statistics;
- generate UUID v4 values;
- return current UTC time.

The core has no dependency on FastMCP and does not perform filesystem, shell, or network operations.

### 2. MCP server layer

File: `src/mcp_toolbox/server.py`

Responsibilities:

- create the `FastMCP("MCP Toolbox")` server;
- expose the current seven MCP tools with typed arguments;
- delegate actual behavior to the core module;
- run the server through `mcp.run()`, using the SDK's default stdio transport.

The server layer is deliberately thin.

### 3. Public Python API

File: `src/mcp_toolbox/__init__.py`

The package re-exports the core functions so consumers can use them directly without MCP.

### 4. MCP client

The client is outside this repository. A compatible client launches `mcp-toolbox` and communicates with it over stdio.

A generic example exists in `examples/client-config.json`.

## Trust boundaries

```text
┌──────────────────────┐
│ MCP-compatible client│
└──────────┬───────────┘
           │ structured MCP messages
           │ local stdio
┌──────────▼───────────┐
│ FastMCP server layer │
│ server.py            │
└──────────┬───────────┘
           │ typed calls
┌──────────▼───────────┐
│ Pure utility core    │
│ core.py              │
└──────────────────────┘
```

The current utility core does not cross into:

- user filesystem access;
- shell/process execution;
- arbitrary network access;
- databases;
- credential storage;
- telemetry.

This narrow boundary is an intentional project property.

## Error handling

Invalid user input raises `ToolboxError` in the core layer.

Examples:

- unsupported hash algorithms;
- over-limit text;
- invalid JSON;
- indentation outside 0–8;
- invalid Base64;
- Base64 that decodes to non-UTF-8 data;
- unsupported UUID versions in the core API.

The MCP wrappers let the SDK expose these failures to the client rather than silently altering inputs.

## Determinism

Most text tools are deterministic for a given input.

Two tools are intentionally non-deterministic:

- `new_uuid` returns a random UUID v4;
- `utc_now` reflects current wall-clock time.

## Test strategy

`tests/test_core.py` tests the pure core directly using Python's standard `unittest` framework.

The current GitHub Actions workflow also performs an import smoke check for the FastMCP server after installing the project.

## Extension guidance

A new tool should normally follow this pattern:

1. implement and validate behavior in `core.py`;
2. add direct unit tests;
3. expose a thin typed wrapper in `server.py`;
4. update README and architecture documentation;
5. consider whether the new capability changes the project's trust boundary.

Capabilities involving files, shell execution, credentials, or network access should not be treated as routine additions because they materially change the security model.
