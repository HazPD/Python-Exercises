#Write a Python program to find a list of strings that have fewer total characters (including repetitions).
def shorter(strings):
    ShortSub = None
    Short_length = float('inf')

    for substring in strings:
        total_length = sum(len(item) for item in substring)
        if total_length < Short_length:
            Short_length = total_length
            ShortSub = substring
    return ShortSub

strings = [['tdsadasdasdasdasd', 'st', 'is', 'narrow'],['I', 'am', 'shorter but wider']]
print(shorter(strings))