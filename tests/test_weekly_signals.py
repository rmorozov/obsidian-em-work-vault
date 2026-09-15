import datetime as dt
import tempfile
import unittest
from pathlib import Path
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from scripts.weekly_signals import main, records


class WeeklySignalsTest(unittest.TestCase):
    def test_records_only_plain_daily_bullets(self):
        text = """## Daily Record
- Release dependency appeared.
- [ ] Call owner.
### Detail
- Cross-team impact confirmed.
## Carry forward
- Not a record.
"""
        self.assertEqual(list(records(text)), [
            "Release dependency appeared.",
            "Cross-team impact confirmed.",
        ])

    def test_iso_week_boundary(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "2026-09-14.md").write_text("## Daily Record\n- Monday.\n")
            (root / "2026-09-20.md").write_text("## Daily Record\n- Sunday.\n")
            (root / "2026-09-21.md").write_text("## Daily Record\n- Next week.\n")
            output = StringIO()
            with patch("sys.argv", ["weekly_signals.py", str(root), "--week", "2026-W38"]):
                with redirect_stdout(output):
                    main()
            self.assertIn("Monday.", output.getvalue())
            self.assertIn("Sunday.", output.getvalue())
            self.assertNotIn("Next week.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
