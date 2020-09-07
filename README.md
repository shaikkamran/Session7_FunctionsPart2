# Session7-FunctionsPart2

![](https://dzone.com/storage/temp/11727498-download.png)

## 1. Returns true if n is a Fibinacci Number, else false
```python
    is_fib = lambda n: is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

```
      
 ## 2.1 add 2 iterables a and b such that a is even and b is odd
```python
    def add_two_iterables_even_odd(itr1, itr2):
        return [(i + j) for i, j in zip(itr1, itr2) if (i % 2 == 0 and j % 2 == 1)]


```

## 2.2 strips every vowel from a string provided (tsai>>t s)
```python
    def remove_vowels_from_string(string):
        return "".join(
            [
                ch
                for ch in string
                if ch not in set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
            ]
        )
```
## 2.3 relu function applied on a 1D array
```python
    def relu_arr(arr):
        return [max(0, i) for i in arr]


```
## 2.4 sigmoid function applied on a 1D array
```python
    def sigmoid_arr(arr):
        sigmoid = lambda x: 1 / (1 + math.exp(-x))
        return [sigmoid(i) for i in arr]

```
## 2.5 takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
```python
    def shift_chars(string):
        return "".join([chr((((ord(ch.lower()) - 97) + 5) % 26) + 97) for ch in string])

```
## 3. A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words
```python
    def check_if_swear_words_present(paragraph):
        swear_words = set(
            {i.replace("\n", "").strip() for i in open("swear_words.txt").readlines()}
        )
        return any(
            word
            for word in re.findall(r"\w+|[^\w\s]", paragraph, re.UNICODE)
            if word in swear_words
        )
```

## 4. Using reduce function:
## 4.1 add only even numbers in a list
```python
    def sum_even_nos(arr):
        return reduce(lambda x, y: x + y if y % 2 == 0 else x, arr, 0)
```

## 4.2 find the biggest character in a string (printable ascii characters)
```python
    def find_biggest_char(string):
        return reduce(lambda res, char: res if ord(res) > ord(char) else char, string)
```

## 4.3 adds every 3rd number in a list
```python
    def add_every_third_no(arr):
        return reduce(
            lambda result, element: result + element,
            list(map(lambda x, y: x if (y + 1) % 3 == 0 else 0, range(len(arr)), arr)),
        )
```

## 5.Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates,
##  where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100
```python
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
```

## 6.Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided.
## Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided PTS:100
```python
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
```

# TEST CASES


## README TEST CASES

* test_readme_exists(): Checks if the README File exists or not.

* test_readme_contents(): Checks if the README has atleast 300 words.

* test_readme_file_for_formatting(): Checks if it has relevant number of '#'

## FILE TEST CASES

* test_function_name_had_cap_letter(): Checks if the Function name was starting with a Capital Letter.

* test_indentations(): Checks if the indentation is proper

## PROGRAM TEST CASES
```python
    
def test_dl_delhi_func():
    assert len(generate_delhi_dl()) == 15
    for dl in generate_delhi_dl():
        assert re.findall(r"DL[0-9][0-9][A-Z][A-Z][1-9][0-9][0-9][0-9]", dl)

```
- test_function_name_had_cap_letter
- test_readme_exists
- test_readme_contents
- test_readme_file_for_formatting
- test_indentations
- test_fibonacci
- test_multiple_fibonacci_nos
- test_addition_even_odd_iterables
- test_vowel_func
- test_relu
- test_sigmoid
- test_shift_chars
- test_swear_words
- test_sum_even_nos
- test_find_biggest_char
- test_add_every_third_no
- test_dl_func
- test_dl_delhi_func