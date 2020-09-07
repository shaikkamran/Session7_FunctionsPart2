# Session6-Poker

![](https://dzone.com/storage/temp/11727498-download.png)

```python
    def generate_deck_from_map_zip():
        """
        Generates a deck of 52 Cards using map,zip and lambda.
        """
        return list(map(lambda x: (x[0], x[1]), zip(vals * 4, suits * 13)))

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