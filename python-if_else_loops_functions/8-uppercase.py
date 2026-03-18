#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for c in str:
        # If character is lowercase a-z, convert to uppercase
        if 'a' <= c <= 'z':
            print("{}".format(chr(ord(c) - 32)), end="")  # 1st print
        else:
            print("{}".format(c), end="")                 # 2nd print
    print()                                              # newline after the loop
