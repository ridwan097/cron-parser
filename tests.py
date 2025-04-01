import unittest
from cron_cli import expand_cron_field, parse_cron

class TestExpandCronField(unittest.TestCase):

    # Happy path tests
    def test_expand_field_star(self):
        self.assertEqual(
            expand_cron_field("*", "minute"),
            list(range(0, 60))
        )

    def test_expand_field_step(self):
        self.assertEqual(
            expand_cron_field("*/15", "minute"),
            [0, 15, 30, 45]
        )

    def test_expand_field_range(self):
        self.assertEqual(
            expand_cron_field("1-5", "hour"),
            [1, 2, 3, 4, 5]
        )

    # Sad path tests
    def test_expand_field_invalid_number(self):
        with self.assertRaises(ValueError):
            expand_cron_field("61", "minute")

    def test_expand_field_invalid_step(self):
        with self.assertRaises(ValueError):
            expand_cron_field("*/abc", "minute")

    def test_expand_field_invalid_literal(self):
        with self.assertRaises(ValueError):
            expand_cron_field("foo", "hour")

    def test_parse_cron_too_few_fields(self):
        with self.assertRaises(ValueError):
            parse_cron("*/15 0 1,15 *")

if __name__ == "__main__":
    unittest.main()
