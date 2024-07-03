#Write a Python program to find strings in a given list containing a given substring.

def IsInWord(letter,char_list):
    words = []
    for i in char_list:
        if str(letter) in i:
            words.append(i)
        else:
            continue
    return words

letter = str(input("Enter substring to search matching words: "))
char_list = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
#TEST CASES 
#['cat', 'car', 'fear', 'center']
#['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print(IsInWord(letter,char_list))