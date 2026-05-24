#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = max(a_dictionary, key=a_dictionary.get)
    return best


'''
a_dictionary = {'John': 12, 'Bob': 14, 'Molly': 16}

max(a_dictionary, key=a_dictionary.get)
Iterates over keys: 'John', 'Bob', 'Molly'
Applies a_dictionary.get to each key:
'John' → 12
'Bob' → 14
'Molly' → 16
Finds max value → 16 → returns key 'Molly'

'''
