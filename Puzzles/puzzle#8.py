#Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators.

def separate(user_input):
    for char in user_input:
        if char != " " or char != ",":
            words.append(char)
            
        if char == " " or char == ",":
            separators.append(char)

words = []
separators = []
user_input = str(input("Enter words, separate it by comma: "))

separate(user_input)
print(" ".join(words))
print(separators)

