import unittest

from day05.part1 import read_input, process_database

INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


class TestIdValidation(unittest.TestCase):

    def test_input(self):
        res = process_database(INPUT)
        self.assertEqual(3, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = process_database(f)
        self.assertEqual(789, result)


if __name__ == "__main__":
    unittest.main()
