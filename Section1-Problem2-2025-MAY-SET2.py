def starts_with_greeting(s):
    """
    Checks whether a given string starts with 'Hello ' or 'Hi '.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string starts with 'Hello ' or 'Hi ', False otherwise.

    Examples:
        >>> starts_with_greeting('Hello there')
        True
        >>> starts_with_greeting('Hi friend')
        True
        >>> starts_with_greeting('Good morning')
        False
        >>> starts_with_greeting('HiThere')
        False
    """
    
    return s.startswith("Hello ") or s.startswith("Hi ")

# #Another Method:

# def starts_with_greeting(s):
  
#     if 'Hello '==s[0:6] or 'Hi '==s[0:3]:
#         return True
#     else:
#         return False

# Check For Greeting Prefix
# Write a function starts_with_greeting(s) that takes a string s and checks whether it starts with "Hello " or "Hi ".
# The function should return True if the string has the specified prefix; otherwise, it should return False. Note the space after the greeting.

# NOTE: This is a function type question, you don't have to take input or print the output, you just have to complete the required function definition.

# Examples

# starts_with_greeting("Hello World") -> True
# Explanation: The string starts with "Hello ".
# starts_with_greeting("Hi There") -> True
# Explanation: The string starts with "Hi ".
# starts_with_greeting("Greetings Earthling") -> False
# Explanation: The string does not start with "Hello " or "Hi ".
# starts_with_greeting("HelloWorld") -> False
# Explanation: The string does not have a space after "Hello".
    
