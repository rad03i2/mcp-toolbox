"""MCP server entry point."""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP
from . import core

mcp = FastMCP("MCP Toolbox")

@mcp.tool()
def hash_text(text: str, algorithm: str = "sha256") -> dict[str, str]:
    """Hash UTF-8 text with sha256, sha512, sha1, or md5."""
    return core.hash_text(text, algorithm)

@mcp.tool()
def format_json(text: str, indent: int = 2, sort_keys: bool = False) -> str:
    """Validate and pretty-print a JSON string."""
    return core.format_json(text, indent, sort_keys)

@mcp.tool()
def base64_encode(text: str) -> str:
    """Encode UTF-8 text as Base64."""
    return core.base64_encode(text)

@mcp.tool()
def base64_decode(value: str) -> str:
    """Decode Base64 into UTF-8 text; rejects malformed input."""
    return core.base64_decode(value)

@mcp.tool()
def text_stats(text: str) -> dict[str, int]:
    """Return character, word, line, and UTF-8 byte counts."""
    return core.text_stats(text)

@mcp.tool()
def new_uuid() -> str:
    """Generate a random RFC 4122 UUID version 4."""
    return core.new_uuid()

@mcp.tool()
def utc_now() -> dict:
    """Return current UTC time as ISO-8601 and Unix seconds."""
    return core.utc_now()

def main() -> None:
    """Run the MCP server over the SDK's default stdio transport."""
    mcp.run()

if __name__ == "__main__":
    main()
