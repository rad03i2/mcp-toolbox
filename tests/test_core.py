import json
import unittest
from unittest.mock import patch
from mcp_toolbox import core

class CoreTests(unittest.TestCase):
    def test_sha256_known_value(self):
        self.assertEqual(core.hash_text("abc")["digest"], "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

    def test_hash_rejects_unknown_algorithm(self):
        with self.assertRaises(core.ToolboxError):
            core.hash_text("x", "nope")

    def test_json_preserves_unicode_and_sorts(self):
        out = core.format_json('{"z":1,"a":"موصل"}', sort_keys=True)
        self.assertEqual(json.loads(out), {"z": 1, "a": "موصل"})
        self.assertLess(out.index('"a"'), out.index('"z"'))

    def test_invalid_json_has_location(self):
        with self.assertRaisesRegex(core.ToolboxError, "line 1"):
            core.format_json("{")

    def test_base64_round_trip_unicode(self):
        text = "Hello مرحبا 👋"
        self.assertEqual(core.base64_decode(core.base64_encode(text)), text)

    def test_base64_rejects_invalid_and_non_utf8(self):
        for value in ("%%%", "/w=="):
            with self.subTest(value=value), self.assertRaises(core.ToolboxError):
                core.base64_decode(value)

    def test_text_stats(self):
        stats = core.text_stats("one two\nثلاثة")
        self.assertEqual(stats["words"], 3)
        self.assertEqual(stats["lines"], 2)
        self.assertGreater(stats["utf8_bytes"], stats["characters"])

    def test_input_limit(self):
        with self.assertRaises(core.ToolboxError):
            core.text_stats("x" * (core.MAX_TEXT + 1))

    def test_uuid_is_v4(self):
        import uuid
        value = uuid.UUID(core.new_uuid())
        self.assertEqual(value.version, 4)

    def test_utc_now_shape(self):
        value = core.utc_now()
        self.assertTrue(value["iso8601"].endswith("Z"))
        self.assertIsInstance(value["unix_seconds"], int)

if __name__ == "__main__":
    unittest.main()
