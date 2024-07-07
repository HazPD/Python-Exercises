#Write a Python program to select a string from a given list of strings with the most unique characters.

def Check_unique(strings):
    max_unique_string = ""
    max_unique_count = 0
    set(strings) #removes duplicate from list
    for i in strings:
        if len(set(i)) > max_unique_count: #length of distinct elements
            max_unique_count = len(set(i))
            max_unique_string = i
    return max_unique_string
   

strings = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
#TEST CASES
#['Green', 'Red', 'Orange', 'Yellow', '', 'White'] - orange
#['cat', 'catatatatctsa', 'abcdefhijklmnopzxcvb', '124259239185125abcdefghijklmnop', '', 'foo', 'unique'] - abcdefhijklmnopzxcvb
print(Check_unique(strings))

