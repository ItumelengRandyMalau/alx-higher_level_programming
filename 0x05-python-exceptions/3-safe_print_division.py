#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        # Attempt to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero exception
        result = None
        print("Division by zero is not allowed.")
    except Exception as e:
        # Handle other exceptions
        result = None
        print(f"An error occurred: {e}")
    finally:
        # Print the result inside the finally block
        print("Inside result: {}".format(result))
        return result
