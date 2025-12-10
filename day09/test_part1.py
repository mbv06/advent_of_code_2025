import unittest

from day09.part1 import read_input, solve

INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""


class Test(unittest.TestCase):

    def test_input(self):
        res = solve(INPUT)
        self.assertEqual(50, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = solve(f)
        self.assertEqual(4786902990, result)


if __name__ == "__main__":
    unittest.main()
