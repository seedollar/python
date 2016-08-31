# Example of how to write unit tests using the unittest package
import unittest
import cap

class TestCap(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one_word(self):
        text = 'hunger'
        result = cap.capitalize_str(text)
        self.assertEqual(result, 'Hunger')

    def test_multiple_words(self):
        text = "this is a unit test"
        result = cap.capitalize_str(text)
        self.assertEqual(result, 'This is a unit test')


if __name__ == '__main__':
    unittest.main()
