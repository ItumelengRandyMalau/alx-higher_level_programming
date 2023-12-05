#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Number of arguments
    num_args = len(argv) - 1

    # Print the number of arguments and the list of arguments
    print("{:d} argument{}{}".format(
        num_args, 's' if num_args != 1 else '', ':' if num_args > 0 else '.'))

    # Print each argument and its position
    for i in range(1, num_args + 1):
        print("{:d}: {}".format(i, argv[i]))
