
def make_word(words, min_len, start_char):
    return "".join([
        w[-1]
        for w in words
        if w and len(w) >= min_len and w.startswith(start_char)
    ])

l, c = input().split()
l = int(l)

n = int(input())
words = [input() for _ in range(n)]

print(make_word(words, l, c))

# #Another Method:

# # Write your code here

# l=[]
# x,y=input().split()
# x=int(x)
# z=int(input())
# while z!=0:
#     z -=1
#     s=input()
#     l.append(s)
    
# s=''
# for i in l:
#     if len(i)>=x:
#         if i[0]==y:
#             s +=i[-1]
            
# print(s)

# Make Word Using Last Characters of Words with Minimum Length and Starting Character
# Given a minimum length l and a character c, consider only those words that have at least l characters and start with the character c (case-sensitive).
# From each selected word take its last character and concatenate them in the order the words appear in the input.
# Output the resulting word. If no word satisfies the criteria, output an empty line.

# Input Format

# The first line contains an integer l (the minimum required length) and a single character c (the required starting letter), separated by a space.
# The second line contains an integer n the number of words that follow.
# Each of the next n lines contains one word.
# Output Format

# A single line the concatenation of the last characters of all qualifying words (or an empty line if there are none).

# Example

# 3 a
# 5
# apple
# ant
# banana
# anchor
# cat
# Output

# etr
# Explanation: apple, ant and anchor satisfy the conditions; their last characters are e, t and r, which form the word etr.

