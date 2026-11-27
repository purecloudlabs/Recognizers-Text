"""Tests for Arabic AM/PM handling in time recognition, including the afternoon marker (العصر)."""

import unittest

from recognizers_suite import Culture, recognize_datetime


class TestArabicTimeAmPm(unittest.TestCase):
    """Arabic times with AM/PM/afternoon markers resolve to the expected 24-hour value."""

    CASES = [
        ("3:00 العصر", "15:00:00"),
        ("3:00 عصرا", "15:00:00"),
        ("3:00 عصراً", "15:00:00"),
        ("ثلاثة عصرا", "15:00:00"),
        ("الساعة 3 العصر", "15:00:00"),
        ("الساعة الثالثة عصرا", "15:00:00"),
        ("ثلاثة مساء", "15:00:00"),
        ("ثلاثة في المساء", "15:00:00"),
        ("ثلاثة صباحا", "03:00:00"),
        ("10:30 صباحا", "10:30:00"),
        ("3:00 مساء", "15:00:00"),
        ("3:00 ص", "03:00:00"),
        ("الرابعة بعد الظهر", "16:00:00"),
        # Arabic-Indic and Extended Arabic-Indic digits
        ("٣:٠٠ العصر", "15:00:00"),
        ("٣:٠٠ عصرا", "15:00:00"),
        ("٣:٠٠ مساء", "15:00:00"),
        ("٣:٠٠ ص", "03:00:00"),
        ("١٠:٣٠ صباحا", "10:30:00"),
        ("الساعة ٣:٣٠ بعد الظهر", "15:30:00"),
        ("۳:۰۰ العصر", "15:00:00"),
    ]

    def test_arabic_time_am_pm(self):
        """Each utterance resolves to its expected time."""
        for text, expected in self.CASES:
            with self.subTest(text=text):
                results = recognize_datetime(text, Culture.Arabic)
                self.assertEqual(expected, results[0].resolution["values"][0]["value"])

    def test_arabic_indic_digits_keep_original_text(self):
        """The matched text is returned with the user's original Arabic-Indic digits."""
        results = recognize_datetime("٣:٠٠ العصر", Culture.Arabic)
        self.assertEqual("٣:٠٠ العصر", results[0].text)
        self.assertEqual(0, results[0].start)
        self.assertEqual(9, results[0].end)
