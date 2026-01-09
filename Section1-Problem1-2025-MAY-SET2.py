
def is_multiple_of_5_not_3(num):
    """
    Checks if a number is a multiple of 5 but not a multiple of 3.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if `num` is a multiple of 5 but not 3, False otherwise.

    Examples:
        >>> is_multiple_of_5_not_3(10)
        True
        >>> is_multiple_of_5_not_3(15)
        False
        >>> is_multiple_of_5_not_3(9)
        False
        >>> is_multiple_of_5_not_3(-25)
        True
    """
    
    return num % 5 == 0 and num % 3 != 0

# #Another Method:

# def is_multiple_of_5_not_3(num):
 
#     if int(num) %5==0 and int(num)%3!=0:
#         return True
#     else:
#         return False

# Check If Multiple of 5 Not 3
# Write a function is_multiple_of_5_not_3 that checks whether a given integer is a multiple of 5 but not a multiple of 3.

# NOTE: This is a function type question, you don't have to take input or print the output, you just have to complete the required function definition.

# For example:

# 10 is a multiple of 5 but not of 3.
# 25 is a multiple of 5 but not of 3.
# -50 is a multiple of 5 but not of 3.
# 15 is a multiple of 5 and also a multiple of 3, so it should not be considered.
# 9 is not a multiple of 5.
# 12 is not a multiple of 5.
