def reversed_squares(l):
    """
    Takes a list of numbers and returns a new list containing the
    squares of the elements in reverse order.

    Args:
        l (list): A list of numbers.

    Returns:
        list: A new list with squares in reverse order.

    Examples:
        >>> reversed_squares([1, 2, 3])
        [9, 4, 1]
        >>> reversed_squares([])
        []
        >>> reversed_squares([-2, 5])
        [25, 4]
    """
    
    return [x**2 for x in l[::-1]]
# #Another Method:

# def reversed_squares(l):
  
#     z=list(map(lambda x:x*x,l))
    
#     return z[::-1]

# Reversed Squares of List Elements
# Write a function reversed_squares that takes a list of numbers l and returns a new list containing the squares of the elements in reverse order.

# NOTE: This is a function type question. You don't have to take input or print the output; you just have to complete the required function definition and return the new list.

# For example:

# If l = [1, 2, 3, 4, 5], the function should return [25, 16, 9, 4, 1].
# If l = [10, 2], the function should return [4, 100].

