#Write a Python program to check the nth-1 string is a proper substring of the nth string in a given list of strings.

def valid_substring(user_list):
        return user_list[len(user_list) -2] in user_list[len(user_list) - 1]

user_list = []

elements_input = str(input("enter strings, separated by comma: "))
element_split = elements_input.split(",")
user_list = element_split

print(valid_substring(user_list))

#TEST CASES 
# Input: a,abb,sfs,oo,de,sfde = True
# Input: a,abb,sfs,oo,ee,sfde = False
#Input: a,abb,sad,ooaaesdfe,sfsdfde,sfsd,sfsdf,qwrew = False
    