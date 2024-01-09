#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
        # Check if the index is valid
    if 0 <= idx < len(my_list):
                        # Use list slicing to delete the element at the specified index
        new_list = my_list[:idx] + my_list[idx+1:]
        return new_list
    return my_list
