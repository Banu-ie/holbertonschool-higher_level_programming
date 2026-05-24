# Python Hello World Exercises

This directory contains several beginner Python exercises focused on printing, string manipulation, and simple concatenation. Each section describes the goal of the exercise and shows the corrected solution.

---

# 0. Hello, print

## Objective

Write a Python script that prints exactly:

```
"Programming is like building a multilingual puzzle
```

followed by a new line.

## Solution

```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

---

# 1. Print integer

## Objective

Print the integer stored in the variable `number`, followed by `Battery street` using **f-strings**, without casting the number to a string.

## Solution

```python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

---

# 2. Print float

## Objective

Print the float stored in the variable `number` with **2 digits of precision** using f-strings.

## Solution

```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

---

# 3. Print string

## Objective

Print 3 times the value of the variable `str` and then print its **first 9 characters**. No loops or conditionals allowed.

## Solution

```python
#!/usr/bin/python3
str = "Holberton School"
print(3 * str)
print(str[:9])
```

---

# 4. Play with strings

## Objective

Print `Welcome to Holberton School!` using the variables `str1` and `str2`. No loops or conditionals allowed.

## Solution

```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```

---

# 5. Copy - Cut - Paste

## Objective

Extract parts of a word:

- `word_first_3`: first 3 letters
- `word_last_2`: last 2 letters
- `middle_word`: word without first and last letters

## Solution

```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```

---

# 6. Create a new sentence

## Objective

Rearrange a string to print:

```
object-oriented programming with Python
```

without creating new variables or using loops.

## Solution

```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[-22:-17] + str[:6]
print(str)
```

---

# 7. Easter Egg

## Objective

Print **The Zen of Python**, by Tim Peters, using the built-in module `this`.

## Solution

```python
#!/usr/bin/python3
import this
```

This prints the full Zen of Python when executed.