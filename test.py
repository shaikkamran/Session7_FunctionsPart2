import inspect
import math
import os
import re
from random import randint

import pytest

import session7_func_part2
from session7_func_part2 import *


def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session7_func_part2, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme_words = [
        word
        for line in open("README.md", "r", encoding="utf-8")
        for word in line.split()
    ]
    assert (
        len(readme_words) >= 500
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting."""
    lines = inspect.getsource(session7_func_part2)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_fibonacci():
    assert is_fib(3)
    assert is_fib(100) == False


def test_multiple_fibonacci_nos():
    pass


def test_addition_even_odd_iterables():
    a = list(range(1, 10))
    b = [i for i in range(100, 1000, 101)]
    assert add_two_iterables_even_odd(a, b) == [203, 407, 611, 815]
    a = list(range(1, 10))
    b = [i for i in range(100, 1000, 100)]
    assert add_two_iterables_even_odd(a, b) == []


def test_vowel_func():
    string = "ilovedogs"
    assert remove_vowels_from_string(string) == "lvdgs"
    assert remove_vowels_from_string("tsai") == "ts"


def test_relu():
    arr = [randint(-100, 100) for _ in range(10)]
    temp_arr = [max(0, i) for i in arr]
    relu_arr(arr) == temp_arr


def test_sigmoid():
    arr = [randint(-100, 100) for _ in range(10)]
    temp_arr = [1 / (1 + math.exp(-i)) for i in arr]
    sigmoid_arr(arr) == temp_arr


def test_shift_chars():
    string = "abcz"
    assert shift_chars(string) == "fghe"


def test_swear_words():
    paragraph1 = "i fucking love this movie ****"
    paragraph2 = "The above line was just used to check the function haha"
    assert check_if_swear_words_present(paragraph1)
    assert check_if_swear_words_present(paragraph2) == False


def test_sum_even_nos():
    arr = range(0, 10)
    assert sum_even_nos(arr) == 20


def test_find_biggest_char():
    string = "abcbdeeeeeeef"
    assert find_biggest_char(string) == "f"


def test_add_every_third_no():
    arr = range(0, 20)
    add_every_third_no(arr) == 57


def test_dl_func():
    assert len(generate_dl()) == 15
    for dl in generate_dl():
        assert re.findall(r"KA[0-9][0-9][A-Z][A-Z][1-9][0-9][0-9][0-9]", dl)


def test_dl_delhi_func():
    assert len(generate_delhi_dl()) == 15
    for dl in generate_delhi_dl():
        assert re.findall(r"DL[0-9][0-9][A-Z][A-Z][1-9][0-9][0-9][0-9]", dl)
