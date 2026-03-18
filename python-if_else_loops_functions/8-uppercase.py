#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for c in str:
        # Print uppercase version if lowercase, else print character as-is
            print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")  
    print() # new line after the loop
