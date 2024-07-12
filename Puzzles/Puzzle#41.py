#Write a Python program to sort numbers based on strings.
num_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six" : 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
}

def sort(strings1):
    NumSort = sorted(strings1, key=lambda x:num_dict[x])
    return NumSort 


strings = "six one four one two three"
strings1 = strings.split(" ")
print(sort(strings1))