# Testing our solutions here.
from datastructures import *
def test_is_balanced():
    assert is_balanced("([]{})") == True
    assert is_balanced("([)]") == False
def test_remove_duplicates():
    assert remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5]) == [2, 3, 4, 5, 6, 7]
def test_word_frequency():
    assert word_frequency("This is a test sentence This sentence is a test") == {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence': 2} 