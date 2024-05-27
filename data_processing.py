#1 

sentence = input("Give me a sentence: ").upper()
print(sentence)

#2
paragraph = input("Give me a paragraph: ").split()
count = int(len(paragraph))
print(f"The number of words in the paragraph is {count}")

#3
string = input("Give me a string: ").isnumeric()
print(string)

#4 
yuh = input("Give me a string with a's in it: ").replace("a","o")
print(yuh)

#5
name = input("Please give me you full name with a space in between: ")
#for this use join method

x = ''.join(([c for c in name if c.isupper()]))
print(x)

#Certainly! Let's break down the code step by step:

# ```python
# name = input("Please give me your full name with a space in between: ")
# ```

# 1. **Input Prompt**: This line asks the user to enter their full name with a space between the first and last name. Whatever the user types in is stored in the variable `name`.

# ```python
# x = ''.join(([c for c in name if c.isupper()]))
# ```

# 2. **List Comprehension**:
#    - `c for c in name if c.isupper()`: This part goes through each character `c` in the `name` string and includes it in a list only if `c` is an uppercase letter.
#    - For example, if `name` is "John Doe", this list comprehension will produce `['J', 'D']`.

# 3. **Join Method**:
#    - `''.join(...)`: The `join` method takes the list of uppercase characters and combines them into a single string. The empty string `''` before `join` means that there will be no characters between the joined elements.
#    - Using our example, `['J', 'D']` becomes `"JD"`.

# So, `x` now holds the initials of the name entered by the user, based on the uppercase letters.

# ```python
# print(x)
# ```

# 4. **Output**: This line prints the value of `x`, which is the initials of the user's name.

# ### Summary

# - The code asks for the user's full name.
# - It then finds all the uppercase letters in the name.
# - These uppercase letters (initials) are joined into a single string.
# - Finally, it prints the initials. 

# If the user enters "John Doe", the output will be "JD".

#6
give = input("Give me a string: ")
print(len(give))
