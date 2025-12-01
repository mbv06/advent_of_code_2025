import unittest
from pathlib import Path

from day01.part2 import calculate_position, read_input


class TestCalculatePosition(unittest.TestCase):
    def test_default(self):
        rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        result = calculate_position(rotations)
        self.assertEqual(result, 6)

    def test_full_rotate_left_from_zero(self):
        result = calculate_position(["L250"], 0)
        self.assertEqual(result, 2)

    def test_key_left(self):
        result = calculate_position(["L250"], 5)
        self.assertEqual(result, 3)

    def test_full_rotate_left_from_same(self):
        result = calculate_position(["L250"], 50)
        self.assertEqual(result, 3)

    def test_rotate_right_zero_result(self):
        result = calculate_position(["R300"], 0)
        self.assertEqual(result, 3)

    def test_orig(self):
        result = calculate_position(["R1000"], 50)
        self.assertEqual(result, 10)

    def test_file(self):
        p = Path(__file__).parent / "input.txt"
        self.assertTrue(p.exists())
        rotations = read_input(p)
        self.assertTrue(rotations)
        result = calculate_position(rotations)
        self.assertEqual(result, 6599)


if __name__ == "__main__":
    unittest.main()
