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

#6
give = input("Give me a string: ")
print(len(give))
