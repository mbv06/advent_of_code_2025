import unittest

from day04.part1 import read_input, to_matrix, calculate_accessed_rolls, process_diagram

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
        self.assertEqual(13, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = process_diagram(f)
        self.assertEqual(1493, result)


if __name__ == "__main__":
    unittest.main()
