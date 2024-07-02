#Write a Python program to find the length of a given list of non-empty strings.
def find_length(given_list):
    length = []
    for i in given_list:
        length.append(len(i))
    return length
        
given_list =['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']

#TEST CASES
#['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
#['cat', 'car', 'fear', 'center','candy','computer']
print(find_length(given_list))