# MCP Toolbox

A small, local **Model Context Protocol (MCP)** server that gives MCP-compatible AI clients a focused set of safe developer utilities. It uses the official Python MCP SDK/FastMCP layer and keeps tool logic separate and directly testable.

**Author:** Radwan Abdulhadi Ahmed · رضوان عبدالهادي أحمد · [@rad03i2](https://github.com/rad03i2)

## Why it exists

AI clients often need tiny deterministic operations—format JSON, calculate a checksum, encode text, count text, create a UUID—without sending data to another web service or granting filesystem/shell access. MCP Toolbox provides those operations over a local MCP server.

## Features

- `hash_text` — SHA-256/SHA-512 plus SHA-1/MD5 for legacy checksum compatibility.
- `format_json` — validate and pretty-print JSON with Unicode preserved.
- `base64_encode` / `base64_decode` — strict UTF-8 Base64 conversion.
- `text_stats` — characters, non-whitespace characters, words, lines, and UTF-8 bytes.
- `new_uuid` — UUID v4 generation.
- `utc_now` — ISO-8601 UTC and Unix timestamp.
- 1,000,000-character input guard for text-processing tools.
- No filesystem access, shell execution, network calls, telemetry, database, or credentials.
- Pure-Python core API plus MCP interface.

## Preview

After configuration, your MCP client can discover tools such as `format_json` and invoke them with structured arguments. This project is a stdio server, so it intentionally has no graphical interface. For a repository screenshot, capture your MCP client's tool-discovery panel showing the locally connected `toolbox` server; never include tokens or private prompts.

## Requirements

- Python 3.10+
- An MCP-compatible client

## Installation

```bash
git clone https://github.com/rad03i2/mcp-toolbox.git
cd mcp-toolbox
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -e .
```

## Client configuration

A generic stdio configuration is included at `examples/client-config.json`:

```json
{
  "mcpServers": {
    "toolbox": {
      "command": "mcp-toolbox",
      "args": []
    }
  }
}
```

The exact configuration file/location depends on your MCP client. If the executable is not visible to the client, use the absolute path to the virtual environment's `mcp-toolbox` executable.

## Usage examples

Once connected, ask your MCP client to use a tool, for example:

- “Use `format_json` on this JSON with indent 2.”
- “Use `hash_text` to calculate SHA-256 for this text.”
- “Use `text_stats` on this paragraph.”

The pure core is also reusable directly:

```python
from mcp_toolbox import hash_text, format_json

print(hash_text("hello"))
print(format_json('{"city":"الموصل","ok":true}'))
```

## Configuration

No environment variables, API keys, or `.env` file are required. The server uses the MCP SDK's default local stdio transport via `mcp.run()`.

## Project structure

```text
src/mcp_toolbox/
  __init__.py     public core API and package metadata
  core.py         validated deterministic utilities
  server.py       FastMCP tool declarations and entry point
tests/test_core.py
examples/client-config.json
.github/workflows/ci.yml
```

## Testing

```bash
python -m compileall -q src tests
python -m unittest discover -s tests -v
```

CI runs compilation, unit tests, and an MCP server import smoke check on Python 3.10, 3.12, and 3.13 across Ubuntu, Windows, and macOS.

## Security & privacy

Processing is local. Tools do not read files, run shell commands, or make network requests. Base64 is not encryption. MD5/SHA-1 are retained only for legacy checksum interoperability; use SHA-256/SHA-512 for integrity work. See [SECURITY.md](SECURITY.md).

## Limitations

- Text utilities intentionally reject inputs above 1,000,000 characters.
- Base64 decoding only accepts payloads that decode to valid UTF-8 text; this is not a binary-file tool.
- `format_json` parses the whole document in memory.
- UUID generation and current time are intentionally non-deterministic tools.
- Client setup differs between MCP hosts; the included config is a generic stdio example.

## Optional roadmap

Possible future additions include safe URL parsing, JSON Pointer helpers, and opt-in resource templates. Arbitrary shell execution and silent filesystem mutation are intentionally outside the project's scope.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Keep additions focused, testable, local-first, and explicit about side effects.

## License

MIT — see [LICENSE](LICENSE).

## Author

**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **[@rad03i2](https://github.com/rad03i2)**

---

# MCP Toolbox — العربية

خادم محلي صغير مبني على **Model Context Protocol (MCP)** يوفّر لعملاء الذكاء الاصطناعي المتوافقين مع MCP مجموعة مركزة من أدوات المطور الآمنة. يستخدم طبقة FastMCP من حزمة MCP الرسمية لبايثون، مع فصل منطق الأدوات عن الخادم لتسهيل الاختبار وإعادة الاستخدام.

## لماذا يوجد المشروع؟

تحتاج تطبيقات الذكاء الاصطناعي كثيرًا إلى عمليات صغيرة وحتمية مثل تنسيق JSON أو حساب بصمة نص أو Base64 أو إحصاءات النص أو إنشاء UUID، دون إرسال البيانات إلى خدمة ويب خارجية أو منح العميل صلاحية الملفات أو سطر الأوامر. يوفر هذا المشروع هذه الوظائف محليًا عبر MCP.

## الميزات

- `hash_text`: حساب SHA-256 وSHA-512، مع SHA-1 وMD5 للتوافق مع البصمات القديمة.
- `format_json`: التحقق من JSON وتنسيقه مع الحفاظ على Unicode.
- `base64_encode` و`base64_decode`: تحويل Base64 صارم لنصوص UTF-8.
- `text_stats`: عدد المحارف والكلمات والأسطر والبايتات.
- `new_uuid`: إنشاء UUID v4.
- `utc_now`: الوقت العالمي UTC بصيغة ISO-8601 وUnix.
- حد مليون محرف لمدخلات أدوات النص لتقليل الاستهلاك العرضي للذاكرة.
- لا وصول للملفات، ولا تنفيذ Shell، ولا شبكة أو تتبع أو قاعدة بيانات أو أسرار.
- واجهة Python مباشرة إلى جانب واجهة MCP.

## المعاينة

بعد ربط الخادم يستطيع عميل MCP اكتشاف الأدوات واستدعاءها بمعاملات منظمة. المشروع خادم stdio ولا يملك واجهة رسومية عمدًا. إذا أردت صورة للمستودع، التقط لوحة الأدوات في عميل MCP وهي تعرض خادم `toolbox` المحلي، مع التأكد من عدم ظهور رموز وصول أو محادثات خاصة.

## المتطلبات والتثبيت

يتطلب Python 3.10 أو أحدث وعميلًا متوافقًا مع MCP.

```bash
git clone https://github.com/rad03i2/mcp-toolbox.git
cd mcp-toolbox
python -m venv .venv
python -m pip install -e .
```

في Windows فعّل البيئة عبر `.venv\Scripts\activate`، وفي Linux/macOS استخدم `source .venv/bin/activate`.

## الاستخدام والإعداد

يوجد مثال جاهز في `examples/client-config.json`. شغّل الخادم بالأمر `mcp-toolbox` من إعداد stdio الخاص بعميلك. موقع ملف إعداد MCP يختلف حسب العميل؛ وإذا لم يجد العميل الأمر فاستخدم المسار المطلق للملف التنفيذي داخل البيئة الافتراضية. لا يحتاج المشروع إلى متغيرات بيئة أو مفاتيح API أو ملف `.env`.

يمكن كذلك استخدام المحرك مباشرة:

```python
from mcp_toolbox import hash_text, text_stats
print(hash_text("مرحبا"))
print(text_stats("أهلاً من الموصل"))
```

## بنية المشروع

`src/mcp_toolbox/core.py` يحوي الأدوات والتحقق، و`server.py` يعرّف أدوات FastMCP، و`tests/` للاختبارات، و`examples/` لإعداد العميل، و`.github/workflows/ci.yml` للتحقق الآلي.

## الاختبارات

```bash
python -m compileall -q src tests
python -m unittest discover -s tests -v
```

يشغّل CI الاختبارات وفحص الاستيراد على Python 3.10 و3.12 و3.13 في Ubuntu وWindows وmacOS.

## الأمان والخصوصية

المعالجة محلية، ولا تقرأ الأدوات ملفات المستخدم ولا تنفذ أوامر النظام ولا تتصل بالشبكة. Base64 ترميز وليس تشفيرًا. MD5 وSHA-1 موجودان فقط للتوافق مع بصمات قديمة؛ استخدم SHA-256 أو SHA-512 لأعمال سلامة البيانات. راجع [SECURITY.md](SECURITY.md).

## القيود

مدخلات النص محدودة بمليون محرف، وBase64 مخصص لنص UTF-8 وليس للملفات الثنائية، وJSON يُحمّل كاملًا في الذاكرة، وإنشاء UUID والوقت الحالي غير حتميين بطبيعتهما، كما تختلف طريقة إعداد MCP من عميل إلى آخر.

## التطوير الاختياري

يمكن مستقبلًا إضافة تحليل آمن لعناوين URL ومساعدات JSON Pointer وقوالب موارد اختيارية. تنفيذ Shell العشوائي أو تعديل الملفات بصمت خارج نطاق المشروع عمدًا.

## المساهمة والترخيص

راجع [CONTRIBUTING.md](CONTRIBUTING.md) للمساهمة. المشروع مرخص وفق MIT؛ راجع [LICENSE](LICENSE).

## المؤلف

**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **[@rad03i2](https://github.com/rad03i2)**
