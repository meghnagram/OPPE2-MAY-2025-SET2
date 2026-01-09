with open(filename) as f:
    k = int(f.readline())

    vowel_count = 0
    for line in f:
        for char in line:
            if char.lower() in "aeiou":
                vowel_count += 1
                if vowel_count % k == 0:
                    print(char.upper(),end='')
                else:
                    print(char.lower(),end='')
            else:
                print(char,end='')

# #Another Method:

# # Write your code to read the file and print the result.
# # use the variable filename for the name of the file.


# with open(filename,'r') as file:
#     num=file.readline().rstrip()
#     num=int(num)
#     counter=0
    
#     for line in file:
#         for ch in line:
#             if ch in 'aeiouAEIOU':
#                 counter +=1
#                 if counter%num==0:
#                     print(ch.upper(),end='')
#                 else:
#                     print(ch.lower(),end='')
#             else:
#                 print(ch,end='')
# Uppercase Every k-th Vowel and lower case other vowels in a File
# Write a program that uppercases every k-th vowel in a text file and lowercase other vowels. Vowels are a, e, i, o, u and the check should be case-insensitive. The case of consonants should be unchanged.

# Assume k is a positive integer.

# The first line of the file contains the integer k.
# Subsequent lines of the file contain the text.
# The vowel count is cumulative across the entire text. For example, if k=3, the 3rd, 6th, 9th, etc., vowels found in the file should be uppercased, regardless of which line they are on.
# NOTE: This is a file-in-stdout type question where the input is read from the file and the output is printed in the standard output.

# Example

# Input(contents of the file)

# 3
# This is a sample text.
# it has many vowels.
# every third one becomes uppercase.
# Output

# This is A sample tExt.
# it has mAny vowels.
# Every third One becOmes uppErcase.

