#Write a Python program to find strings in a given list starting with a given prefix.
def isPrefix(prefix):
    words = []
    for i in char_list:
        if prefix in str(i):
            words.append(i)
    return words

prefix = str(input("Enter prefix: "))
char_list = ['cat', 'car', 'fear', 'center','candy']

print(isPrefix(prefix))