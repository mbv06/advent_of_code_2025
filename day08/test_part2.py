import unittest

from day08.part2 import read_input, solve_junctions

INPUT = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


class TestIdValidation(unittest.TestCase):

    def test_input(self):
        res = solve_junctions(INPUT)
        self.assertEqual(25272, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = solve_junctions(f)
        self.assertEqual(9271575747, result)


if __name__ == "__main__":
    unittest.main()
