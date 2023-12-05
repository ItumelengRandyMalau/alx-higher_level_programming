#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    # Convert and sum all arguments
    result = sum(int(arg) for arg in argv[1:])

    # Print the result
    print(result)
