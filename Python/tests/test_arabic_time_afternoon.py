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
    ]

    def test_arabic_time_am_pm(self):
        """Each utterance resolves to its expected time."""
        for text, expected in self.CASES:
            with self.subTest(text=text):
                results = recognize_datetime(text, Culture.Arabic)
                self.assertEqual(expected, results[0].resolution["values"][0]["value"])
