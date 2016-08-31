# Example of how to use the nose test package
# To run the test, execute the following command: nosetests nose_example.py
import cap
from nose.tools import eq_

def test_one_word():
    text = 'hunger'
    result = cap.capitalize_str(text)
    eq_(result, 'Hunger')

def test_multiple_words():
    text = "this is a nose unit test"
    result = cap.capitalize_str(text)
    eq_(result, 'This is a nose unit test')




