import unittest

from day10.part1 import read_input, solve

INPUT = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""


class Test(unittest.TestCase):

    def test_input(self):
        res = solve(INPUT)
        self.assertEqual(7, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = solve(f)
        self.assertEqual(415, result)


if __name__ == "__main__":
    unittest.main()
