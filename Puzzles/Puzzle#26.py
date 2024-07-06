#Write a Python program to find the largest number where commas or periods are decimal points.
def find(int_list):
    Highest = []
    temp = [i.replace(',','.') for i in int_list]
    Highest = max(temp)
    return Highest

    
int_list = ['100', '102,1', '101.1','105,3']
print(find(int_list))