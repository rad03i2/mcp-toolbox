"""Pure utility functions used by MCP Toolbox."""
from __future__ import annotations

import base64
import hashlib
import json
import re
import uuid
from datetime import datetime, timezone
from typing import Any

MAX_TEXT = 1_000_000
_HASHES = {"sha256": hashlib.sha256, "sha512": hashlib.sha512, "sha1": hashlib.sha1, "md5": hashlib.md5}

class ToolboxError(ValueError):
    """Raised for invalid user input."""

def _text(value: str) -> str:
    if not isinstance(value, str):
        raise ToolboxError("value must be a string")
    if len(value) > MAX_TEXT:
        raise ToolboxError(f"input exceeds {MAX_TEXT} characters")
    return value

def hash_text(text: str, algorithm: str = "sha256") -> dict[str, str]:
    text = _text(text)
    algorithm = algorithm.lower()
    if algorithm not in _HASHES:
        raise ToolboxError("algorithm must be one of: sha256, sha512, sha1, md5")
    return {"algorithm": algorithm, "digest": _HASHES[algorithm](text.encode("utf-8")).hexdigest()}

def format_json(text: str, indent: int = 2, sort_keys: bool = False) -> str:
    text = _text(text)
    if not 0 <= indent <= 8:
        raise ToolboxError("indent must be between 0 and 8")
    try:
        value = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ToolboxError(f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    return json.dumps(value, ensure_ascii=False, indent=indent, sort_keys=sort_keys)

def base64_encode(text: str) -> str:
    return base64.b64encode(_text(text).encode("utf-8")).decode("ascii")

def base64_decode(value: str) -> str:
    value = _text(value)
    try:
        raw = base64.b64decode(value, validate=True)
        return raw.decode("utf-8")
    except (ValueError, UnicodeDecodeError) as exc:
        raise ToolboxError("value is not valid Base64-encoded UTF-8") from exc

def text_stats(text: str) -> dict[str, int]:
    text = _text(text)
    return {
        "characters": len(text),
        "characters_no_whitespace": sum(not c.isspace() for c in text),
        "words": len(re.findall(r"\S+", text)),
        "lines": 0 if not text else text.count("\n") + 1,
        "utf8_bytes": len(text.encode("utf-8")),
    }

def new_uuid(version: int = 4) -> str:
    if version != 4:
        raise ToolboxError("only UUID version 4 is supported")
    return str(uuid.uuid4())

def utc_now() -> dict[str, Any]:
    now = datetime.now(timezone.utc)
    return {"iso8601": now.isoformat().replace("+00:00", "Z"), "unix_seconds": int(now.timestamp())}
