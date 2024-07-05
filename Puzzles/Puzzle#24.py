#Write a Python program to create a list whose ith element is the maximum of the first i elements from an input list.

def Check(Nums):
    Highest = []
    Top = Nums[0]
    for i in range(len(Nums)):
        Top = max(Top,Nums[i])
        Highest.append(Top)
    return Highest

Nums = [0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0]
#TEST CASES
#[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0] = [0, 0, 3, 8, 8, 9, 9, 14, 14, 14, 14, 14, 14, 17, 41, 41, 41, 41, 41, 41]
#[6, 5, 4, 3, 2, 1] = [6, 6, 6, 6, 6, 6]
#[1, 19, 5, 15, 5, 25, 5] = [1, 19, 19, 19, 19, 25, 25]
print(Check(Nums))