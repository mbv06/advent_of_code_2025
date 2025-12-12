import unittest

from day11.part1 import read_input, solve

INPUT = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""


class Test(unittest.TestCase):

    def test_input(self):
        res = solve(INPUT)
        self.assertEqual(5, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = solve(f)
        self.assertEqual(749, result)


if __name__ == "__main__":
    unittest.main()
