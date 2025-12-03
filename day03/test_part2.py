import unittest

from day03.part2 import process_backets, read_input

INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111"""


class TestIdValidation(unittest.TestCase):

    def test_input(self):
        res = process_backets(INPUT)
        self.assertEqual(3121910778619, res)

    def test_joltage(self):
        self.assertEqual(888911112111, process_backets("818181911112111"))

    def test_first_last(self):
        self.assertEqual(811111111119, process_backets("811111111111119"))

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = process_backets(f)
        self.assertEqual(171741365473332, result)


if __name__ == "__main__":
    unittest.main()
