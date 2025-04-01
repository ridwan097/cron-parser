import unittest
from cron_cli import expand_cron_field

class TestExpandCronField(unittest.TestCase):

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

if __name__ == "__main__":
    unittest.main()
