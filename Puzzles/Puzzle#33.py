# Write a Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
def check(Strings):
    positions = []
    vowel = ['A','E','I','O','U','a','e','i','o','u']
    for i,j in enumerate(Strings):
        if  i % 2 == 0 and j in vowel:
            positions.append(i)
    return positions

strings = "w3rEsOUrcE"
Strings = ([*strings])
print(check(Strings))