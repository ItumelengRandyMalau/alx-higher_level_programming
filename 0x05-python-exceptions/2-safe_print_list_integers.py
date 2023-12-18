#!/usr/bin/python
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            # Try to print the element as an integer using "{:d}".format()
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        print()  # Print a new line after printing all integers
        return counter
    except (TypeError, IndexError):
        print()  # Print a new line in case of an exception
        return counter
