"""Homework 9.1."""

from homework09 import (
    add_numbers,
    calculate_average,
    reverse_string,
    find_longest_word,
    find_substring,
)


# Тести для Task 1: add_numbers
def test_add_numbers_positive():
    """Positive numbers test for Task 1."""
    assert add_numbers(3, 5) == 8


def test_add_numbers_negative():
    """Negative numbers test for Task 1."""
    assert add_numbers(-3, -5) == -8


def test_add_numbers_mixed():
    """Mixed numbers test for Task 1."""
    assert add_numbers(10, -5) == 5


def test_add_numbers_zero():
    """Zero test for Task 1."""
    assert add_numbers(0, 5) == 5


# Тести для Task 2: calculate_average
def test_calculate_average_non_empty_list():
    """Calculate average - positive test."""
    assert calculate_average([1, 2, 3, 4, 5]) == 3


def test_calculate_average_empty_list():
    """Calculate average - empty list test."""
    assert calculate_average([]) == 0


def test_calculate_average_single_element():
    """Calculate average -  list list with ione element test."""
    assert calculate_average([10]) == 10.0


def test_calculate_average_negative_numbers():
    """Calculate average - negative numbers test."""
    assert calculate_average([-10, -20, -30]) == -20.0


# Тести для Task 3: reverse_string
def test_reverse_string_non_empty():
    """Reverse string - positive test."""
    assert reverse_string('abc') == 'cba'


def test_reverse_string_empty():
    """Reverse string - empty list test."""
    assert reverse_string('') == ''


def test_reverse_string_special_chars():
    """Reverse string - special chars test."""
    assert reverse_string('!@#') == '#@!'


# Тести для Task 4: find_longest_word
def test_find_longest_word_multiple_words():
    """Find the longest word - positive test."""
    words = ['short', 'longer', 'longest']
    assert find_longest_word(words) == 'longest'


def test_find_longest_word_empty_list():
    """Find the longest word - empty list test."""
    assert find_longest_word([]) is None


def test_find_longest_word_single_word():
    """Find the longest word - single word test."""
    assert find_longest_word(['word']) == 'word'


# Тести для Task 5: find_substring
def test_find_substring_found():
    """Find substring - positive test."""
    assert find_substring('hello world', 'world') == 6


def test_find_substring_not_found():
    """Find substring - negative test."""
    assert find_substring('hello world', 'python') == -1


def test_find_substring_empty_substring():
    """Find substring - empty substring test."""
    assert find_substring('hello world', '') == 0


def test_find_substring_empty_string():
    """Find substring - empty strings test."""
    assert find_substring('', 'world') == -1


def test_find_substring_identical_strings():
    """Find substring - identical substring test."""
    assert find_substring('hello', 'hello') == 0
