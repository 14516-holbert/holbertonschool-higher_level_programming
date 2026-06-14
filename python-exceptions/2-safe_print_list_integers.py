#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list and only integers.
    
    Args:
        my_list (list): The list to iterate through.
        x (int): The number of elements to access.
        
    Returns:
        int: The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Silently skip elements that cannot be formatted as integers
            pass
            
    print("")  # Prints the trailing new line
    return count
