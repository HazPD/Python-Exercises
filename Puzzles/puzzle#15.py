#Write a Python program to find the longest string in a given list of strings.
def find_long(char_list):
    longest = ""
    for i in char_list:
        if len(i) > len(longest):
            longest = i
    return longest
                
char_list = ['cat', 'car', 'fear', 'center']

print(find_long(char_list)) 