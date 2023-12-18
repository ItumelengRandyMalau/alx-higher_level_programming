#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        item = 0
        for i in range(x):
            print(my_list[i], end="")
            item += 1
        print()  # Print a new line after all elements
        return item
    except IndexError:
        print()  # Print a new line in case of an IndexError
        return item
