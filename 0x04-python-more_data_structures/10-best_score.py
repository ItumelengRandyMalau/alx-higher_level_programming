#!/usr/bin/python3
def best_score(a_dictionary):
    # Check if the dictionary is not empty
    if a_dictionary:
        # Find the key with the maximum value
        max_key = max(a_dictionary, key=a_dictionary.get)
        return max_key
    else:
        # Return None if the dictionary is empty
        return None
