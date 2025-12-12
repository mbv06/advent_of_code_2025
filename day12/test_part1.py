import unittest

from day12.part1 import read_input, solve

INPUT = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""


class Test(unittest.TestCase):

    def test_input(self):
        res = solve(INPUT)
        self.assertEqual(2, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = solve(f)
        self.assertEqual(528, result)


if __name__ == "__main__":
    unittest.main()
