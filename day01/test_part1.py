import unittest
from pathlib import Path

from day01.part1 import calculate_position, read_input


class TestCalculatePosition(unittest.TestCase):
    def test_default(self):
        rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        result = calculate_position(rotations)
        self.assertEqual(result, 3)

    def test_key_left(self):
        result = calculate_position(["L100"], 0)
        self.assertEqual(result, 1)

    def test_file(self):
        p = Path(__file__).parent / "input.txt"
        self.assertTrue(p.exists())
        rotations = read_input()
        self.assertTrue(rotations)
        result = calculate_position(rotations)
        self.assertEqual(result, 1105)


if __name__ == "__main__":
    unittest.main()
