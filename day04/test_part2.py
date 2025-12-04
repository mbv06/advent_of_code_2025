import unittest

from day04.part2 import read_input, to_matrix, process_diagram

INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


class TestIdValidation(unittest.TestCase):

    def test_to_matrix(self):
        matrix = [
            ['.', '.', '@', '@', '.', '@', '@', '@', '@', '.'],
            ['@', '@', '@', '.', '@', '.', '@', '.', '@', '@'],
            ['@', '@', '@', '@', '@', '.', '@', '.', '@', '@'],
            ['@', '.', '@', '@', '@', '@', '.', '.', '@', '.'],
            ['@', '@', '.', '@', '@', '@', '@', '.', '@', '@'],
            ['.', '@', '@', '@', '@', '@', '@', '@', '.', '@'],
            ['.', '@', '.', '@', '.', '@', '.', '@', '@', '@'],
            ['@', '.', '@', '@', '@', '.', '@', '@', '@', '@'],
            ['.', '@', '@', '@', '@', '@', '@', '@', '@', '.'],
            ['@', '.', '@', '.', '@', '@', '@', '.', '@', '.'],
        ]
        self.assertEqual(matrix, to_matrix(INPUT))

    def test_input(self):
        res = process_diagram(INPUT)
        self.assertEqual(43, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = process_diagram(f)
        self.assertEqual(9194, result)


if __name__ == "__main__":
    unittest.main()
