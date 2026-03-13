# Python Hello World Exercises

This directory contains several beginner Python exercises focused on printing, string manipulation, and simple concatenation. Each section describes the goal of the exercise and how the code achieves it.

---

# Hello, print

## Objective

Write a Python script that prints exactly:

```
"Programming is like building a multilingual puzzle
```

followed by a new line.

## Solution

Use the `print` function:

```python
print("Programming is like building a multilingual puzzle")
```

This prints the required string and ends with a newline.

---

# Print integer

## Objective

Print the integer stored in the variable `number`, followed by `Battery street`, using **f-strings**. Do not cast `number` to a string.

## Solution

```python
number = 98
print(f"{number} Battery street")
```

This outputs:

```
98 Battery street
```

---

# Print float

## Objective

Print the float stored in the variable `number` with **2 digits of precision** using f-strings.

## Solution

```python
number = 3.14159
print(f"Float: {number:.2f}")
```

This outputs:

```
Float: 3.14
```

---

# Print string

## Objective

Print 3 times the value of the variable `str` and then print its **first 9 characters**. No loops or conditionals allowed.

## Solution

```python
str = "Holberton School"
print(str * 3)
print(str[:9])
```

This outputs:

```
Holberton SchoolHolberton SchoolHolberton School
Holberton
```

---

# Play with strings

## Objective

Print `Welcome to Holberton School!` using the variables `str1` and `str2`. No loops or conditionals allowed.

## Solution

```python
str1 = "Welcome to "
str2 = "Holberton School!"
print(str1 + str2)
```

This outputs:

```
Welcome to Holberton School!
```

---

# Copy - Cut - Paste

## Objective

Extract parts of a word:

- `word_first_3`: first 3 letters
- `word_last_2`: last 2 letters
- `middle_word`: word without first and last letters

## Solution

```python
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]

print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

This outputs:

```
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
```

---

# Create a new sentence

## Objective

Print `object-oriented programming with Python` without creating new variables or using string literals.

## Solution

```python
str1 = "object-oriented"
str2 = " programming with Python"
print(str1 + str2)
```

This outputs:

```
object-oriented programming with Python
```

---

# Easter Egg

## Objective

Print **The Zen of Python**, by Tim Peters, using the built-in module `this`. Maximum 98 characters for the script.

## Solution

```python
import this
```

This prints:

```
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
