#Write a Python program to split a given string (s) into strings if there is a space in s, otherwise split on commas if there is a comma, otherwise return the list of lowercase letters in odd order (order of a = 0, b = 1, etc.).

def check(InputString):
    output = []
    odd_list = []
    for char in InputString:
        if " " in InputString:
            x = InputString.split(" ")
            output = x
            break
        elif "," in InputString:
            y = InputString.split(",")
            output = y
            break
        else:
            odd_list = InputString
            for i, value in enumerate(odd_list):
                if i % 2 == 1:
                    output.append((value))
            break
    return output

InputString = "abcdefghij"

print(check(InputString))

    
    



