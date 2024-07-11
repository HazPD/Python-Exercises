#Write a Python program to sort the numbers in a given list by the sum of their digits.
def check(int_list):
    return sorted(int_list,key = lambda n:sum(int(c) for c in str(n)))

int_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(check(int_list))