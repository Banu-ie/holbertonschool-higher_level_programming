#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    return list(map(lamba x: x*number, my_list))


# -----------------------------
# multiply_list_map explanation
# -----------------------------
# 1. map(function, iterable)
#    - Built-in function that applies 'function' to every element of 'iterable'
#    - Returns a map object (lazy iterator)
#
# 2. lambda x: x * number
#    - Anonymous inline function
#    - 'x' is each element from my_list
#    - Returns x multiplied by number
#
# 3. my_list
#    - Iterable to loop over
#
# 4. Step by step
#    my_list = [1,2,3], number = 4
#    map applies lambda to each element:
#        1*4 → 4
#        2*4 → 8
#        3*4 → 12
#    map object → list(result) → [4, 8, 12]
#
# 5. Key points
#    - lambda is an inline function
#    - map applies function to each element without a loop
#    - list() converts the map object to a normal list
