import unittest

from day11.part2 import read_input, solve

INPUT = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


class Test(unittest.TestCase):

    def test_input(self):
        res = solve(INPUT)
        self.assertEqual(2, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = solve(f)
        self.assertEqual(420257875695750, result)


if __name__ == "__main__":
    unittest.main()
