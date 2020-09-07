import math
from functools import reduce, partial
import random
import re

# A utility function that returns true if x is perfect square
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x


# 1. Returns true if n is a Fibinacci Number, else false
is_fib = lambda n: is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# 2. Using list comprehension (and zip/lambda/etc if required) write expressions that
# 2.1 add 2 iterables a and b such that a is even and b is odd
def add_two_iterables_even_odd(itr1, itr2):
    # return list(
    #     filter(
    #         None,
    #         map(
    #             lambda x, y: x + y if (x % 2 == 0 and y % 2 == 1) else None, itr1, itr2
    #         ),
    #     )
    # )
    return [(i + j) for i, j in zip(itr1, itr2) if (i % 2 == 0 and j % 2 == 1)]


# 2.2 strips every vowel from a string provided (tsai>>t s)
def remove_vowels_from_string(string):
    # f = (
    #     lambda x: x
    #     if x not in {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    #     else None
    # )
    # return "".join(list(filter(None, map(f, string))))

    return "".join(
        [
            ch
            for ch in string
            if ch not in set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        ]
    )


# 2.3 acts like a ReLU function for a 1D array
def relu_arr(arr):
    return [max(0, i) for i in arr]


# 2.4 acts like a sigmoid function for a 1D array
def sigmoid_arr(arr):
    sigmoid = lambda x: 1 / (1 + math.exp(-x))
    return [sigmoid(i) for i in arr]


# 2.5 takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
def shift_chars(string):
    return "".join([chr((((ord(ch.lower()) - 97) + 5) % 26) + 97) for ch in string])


# 3. A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words
def check_if_swear_words_present(paragraph):
    swear_words = set(
        {i.replace("\n", "").strip() for i in open("swear_words.txt").readlines()}
    )
    return any(
        word
        for word in re.findall(r"\w+|[^\w\s]", paragraph, re.UNICODE)
        if word in swear_words
    )


# 4. Using reduce function:
# 4.1 add only even numbers in a list
def sum_even_nos(arr):
    return reduce(lambda x, y: x + y if y % 2 == 0 else x, arr, 0)


# 4.2 find the biggest character in a string (printable ascii characters)
def find_biggest_char(string):
    return reduce(lambda res, char: res if ord(res) > ord(char) else char, string)


# 4.3 adds every 3rd number in a list
def add_every_third_no(arr):
    return reduce(
        lambda result, element: result + element,
        list(map(lambda x, y: x if (y + 1) % 3 == 0 else 0, range(len(arr)), arr)),
    )


# 5.Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates,
#  where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100


def generate_random_dl_list():
    random_CAP_letter = lambda: chr(random.randint(65, 90))

    return [
        "KA"
        + str(random.randint(10, 99))
        + random_CAP_letter()
        + random_CAP_letter()
        + str(random.randint(1000, 9999))
        for _ in range(15)
    ]


# 6.Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided.
# Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:100


def generate_dl(state_code="KA", start=1000, end=9999):
    random_CAP_letter = lambda: chr(random.randint(65, 90))

    return [
        state_code
        + str(random.randint(10, 99))
        + random_CAP_letter()
        + random_CAP_letter()
        + str(random.randint(start, end))
        for _ in range(15)
    ]


generate_delhi_dl = partial(generate_dl, "DL")
generate_karnataka_dl_within_range = partial(generate_dl, start=1000, end=9999)
