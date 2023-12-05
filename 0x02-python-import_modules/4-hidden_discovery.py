#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in hidden_4 module
    module_names = dir(hidden_4)

    # Filter names that do not start with __ and print them in alphabetical order
    for name in sorted(name for name in module_names if not name.startswith('__')):
        print(name)
