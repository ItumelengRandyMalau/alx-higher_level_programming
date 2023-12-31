#!/usr/bin/python3
import sys  # Import sys module to access stderr

def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
