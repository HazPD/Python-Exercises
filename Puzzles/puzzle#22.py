#Write a Python program to compute the sum of the ASCII values of the upper-case characters in a given string.
def check(UserString):
    AsciiSum = 0
    for char in UserString:
        if char.isupper():
            a = ord(char)
            AsciiSum += a
    return AsciiSum 

UserString = "JavaScript"
print(check(UserString))

#TEST CASES
#PytHon ExerciSEs = 373
#JavaScript = 157