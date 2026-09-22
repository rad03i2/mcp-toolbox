# Contributing / المساهمة

Contributions are welcome when they keep the server small, local, deterministic, and safe.

1. Fork the repository and create a focused branch.
2. Use Python 3.10+ and install with `python -m pip install -e .`.
3. Add or update tests for every behavior change.
4. Run `python -m compileall -q src tests` and `python -m unittest discover -s tests -v`.
5. Update both English and Arabic README sections when user-facing behavior changes.
6. Open a focused pull request explaining the behavior and security implications.

Please do not add telemetry, embedded credentials, arbitrary shell execution, or tools that silently mutate user data.

---

نرحب بالمساهمات التي تحافظ على الخادم صغيرًا ومحليًا وحتميًا وآمنًا. أضف اختبارات لأي تغيير سلوكي، وشغّل أوامر التحقق أعلاه، وحدّث قسمي README الإنجليزي والعربي عند تغيير السلوك الظاهر للمستخدم. لا تضف تتبعًا أو أسرارًا أو تنفيذ أوامر نظام عشوائية أو أدوات تعدّل بيانات المستخدم بصمت.
