#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    return sum(unique_numbers)


'''
    def uniq_add(my_list=[]):
        total = 0
        new_list = []

        for i in my_list:
            if i is not in new_list:
                total += i
                new_list.append(i)

            return total
'''
