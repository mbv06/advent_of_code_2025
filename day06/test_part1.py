import unittest

from day06.part1 import read_input, calculate_grand_total

INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


class TestIdValidation(unittest.TestCase):

    def test_input(self):
        res = calculate_grand_total(INPUT)
        self.assertEqual(4277556, res)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = calculate_grand_total(f)
        self.assertEqual(5595593539811, result)


if __name__ == "__main__":
    unittest.main()
