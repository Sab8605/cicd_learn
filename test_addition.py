"""Tests for addition.py module."""

from addition import add, string_add


# Tests for add() function

def test_add_positive_numbers():
    assert add(1, 2) == 3

def test_add_negative_numbers():
    assert add(-1, -2) == -3

def test_add_zero():
    assert add(0, 5) == 5

def test_add_floats():
    assert add(1.5, 2.5) == 4.0


# Tests for string_add() function

def test_string_add_basic():
    assert string_add("Hello", "World") == "HelloWorld"

def test_string_add_empty():
    assert string_add("", "test") == "test"

def test_string_add_with_space():
    assert string_add("Hello ", "World") == "Hello World"
