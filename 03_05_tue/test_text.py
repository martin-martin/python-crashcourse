import text
import unittest


class TestText(unittest.TestCase):

    def setUp(self):
        self.my_list = [1, 2, 3, 5, 42]

    def tearDown(self):
        pass

    def test_if_input_to_is_palindrom_returns_false_if_input_is_empty(self):
        self.assertIs(text.is_palindrome(''), False)

    def test_input_of_only_whitespace_chars(self):
        self.assertIs(text.is_palindrome('      '), False)
        self.assertIs(text.is_palindrome('  '), False)
        self.assertIs(text.is_palindrome(' '), False)

    def test_if_input_returns_false_if_single_char(self):
        chars = "abcdefg"
        for c in chars:
            self.assertIs(text.is_palindrome(c), False)

    def test_that_function_returns_true_if_word_is_palindrome(self):
        self.assertIs(text.is_palindrome('abba'), True)
        self.assertIs(text.is_palindrome('racecar'), True)
        self.assertIs(text.is_palindrome('roiior'), True)

    def test_returns_false_if_word_is_not_a_palindrome(self):
        self.assertIs(text.is_palindrome('word'), False)
        self.assertIs(text.is_palindrome('Caden'), False)

    # returns False if string contains a number



























# import unittest
# import text
#
#
# class TestText(unittest.TestCase):
#
#     def test_whether_palindromes_are_found(self):
#         self.assertTrue(text.is_palindrome('abba'))
#         self.assertTrue(text.is_palindrome('racecar'))
#         self.assertFalse(text.is_palindrome('hello'))
#
#     def test_if_word_starts_with_character(self):
#         self.assertTrue(text.starts_with('hello', 'h'))
#         self.assertFalse(text.starts_with('hello', 'y'))
#
#     def test_counting_characters_in_word(self):
#         self.assertEqual(text.count_characters('martin'), 6)
#         self.assertEqual(text.count_characters('codingnomads'), 12)
#
#
# if __name__ == '__main__':
#     unittest.main()
