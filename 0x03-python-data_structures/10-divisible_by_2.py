#!/usr/bin/python3

def divisible_by_2(my_list=[]):
        # Use list comprehension to create a new list of True or False
    result_list = [num % 2 == 0 for num in my_list]

    return result_list
