import unittest

from day03.part1 import process_backets, max_joltage, read_input

INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


class TestIdValidation(unittest.TestCase):

    def test_input(self):
        res = process_backets(INPUT)
        self.assertEqual(357, res)

    def test_joltage(self):
        self.assertEqual("92", max_joltage("818181911112111"))

    def test_first_last(self):
        self.assertEqual("89", max_joltage("811111111111119"))

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = process_backets(f)
        self.assertEqual(17316, result)


if __name__ == "__main__":
    unittest.main()
