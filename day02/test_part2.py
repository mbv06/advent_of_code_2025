import unittest

from day02.part2 import is_invalid, process_ranges


class TestIdValidation(unittest.TestCase):

    def test_single_repeated(self):
        self.assertTrue(is_invalid("1111111"))

    def test_invalid_repeated(self):
        self.assertTrue(is_invalid("12341234"))
        self.assertTrue(is_invalid("123123123"))
        self.assertTrue(is_invalid("1212121212"))

    def test_valid_base(self):
        self.assertTrue(is_invalid("11"))
        self.assertTrue(is_invalid("111"))
        self.assertTrue(is_invalid("1010"))
        self.assertTrue(is_invalid("222222"))
        self.assertTrue(is_invalid("1188511885"))
        self.assertTrue(is_invalid("446446"))
        self.assertTrue(is_invalid("38593859"))
        self.assertTrue(is_invalid("824824824"))
        self.assertTrue(is_invalid("2121212121"))

    def test_failed(self):
        self.assertFalse(is_invalid("1000"))
        self.assertFalse(is_invalid("101"))
        self.assertFalse(is_invalid("222220"))
        self.assertFalse(is_invalid("104510"))
        self.assertFalse(part2y.is_invalid("104510"))
        self.assertFalse(is_invalid("422468141"))
        self.assertFalse(is_invalid("9797977797"))

    def test_valid(self):
        self.assertFalse(is_invalid("101"))

    def test_sequence(self):
        seq = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        result = process_ranges(seq)
        self.assertEqual(4174379265, result)

    # def test_file(self):  #     f = read_input()  #     self.assertTrue(f)  #     result = process_ranges(f)  #     self.assertEqual(70187097315, result)


if __name__ == "__main__":
    unittest.main()
