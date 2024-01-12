#!/usr/bin/python3
'''a class named MyList that inherits from list,
    with a public instance method,
    that prints the list sorted in ascending order.
    it assumes that all elements of the list will be of type    int'''


class MyList(list):

    def print_sorted(self):

        print(sorted(self))
