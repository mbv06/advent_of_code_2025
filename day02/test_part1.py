import unittest

from day02.part1 import is_invalid, process_ranges, read_input


class TestIdValidation(unittest.TestCase):

    def test_invalid_repeated(self):
        self.assertTrue(is_invalid("55"))
        self.assertTrue(is_invalid("6464"))
        self.assertTrue(is_invalid("123123"))

    def test_valid(self):
        self.assertFalse(is_invalid("101"))

    def test_sequence(self):
        seq = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        result = process_ranges(seq)
        self.assertEqual(result, 1227775554)

    def test_file(self):
        f = read_input()
        self.assertTrue(f)
        result = process_ranges(f)
        self.assertEqual(result, 54234399924)

if __name__ == "__main__":
    unittest.main()
