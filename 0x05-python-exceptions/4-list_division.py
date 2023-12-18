#!/usr/bin/python
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    
    for i in range(list_length):
        try:
            # Try to perform the division element by element
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0
            
            # Check if both elements are numeric
            if not (isinstance(element_1, (int, float)) and isinstance(element_2, (int, float))):
                raise TypeError("wrong type")

            # Check if the divisor is not zero
            if element_2 == 0:
                raise ZeroDivisionError("division by 0")

            result = element_1 / element_2
        except TypeError as e:
            # Handle wrong type exception
            result = 0
            print(e)
        except ZeroDivisionError as e:
            # Handle division by zero exception
            result = 0
            print(e)
        except IndexError:
            # Handle out of range exception
            result = 0
            print("out of range")
        finally:
            # Append the result to the result_list
            result_list.append(result)

    return result_list
