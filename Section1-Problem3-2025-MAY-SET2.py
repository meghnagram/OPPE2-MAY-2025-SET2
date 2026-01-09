def combine_edges(s: str) -> str:
    '''
    Create a new string made of the first two and last two 
    characters from the given string.

    Arguments:
    s: str - a string.

    Return: str - a new string made of the first and last two characters.
    '''
    
    
    if len(s) < 4:
        return ""
    return s[:2] + s[-2:]
    
# #Another Method:

# def combine_edges(s: str) -> str:

#     if len(s)<4:
#         return ''
#     else:
#         return s[0:2]+s[-2:]

# Combine First and Last Two Chars of a string
# Given a string s, create and return a new string made of the first two and last two characters from the original string.

# If the string length is less than four, return an empty string.

# Example

# s = 'Programming'
# The first two characters are 'Pr' and the last two are 'ng'. The result is 'Prng'.
    

