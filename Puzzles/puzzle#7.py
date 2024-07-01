#Write a Python program to check a given list of integers where the sum of the first i integers is i.

def see_sum(li,i):
    cumulative_sum = 0
    for index in range(i):
        cumulative_sum += li[index]
        if cumulative_sum > i:
            return False
    return cumulative_sum == i


nums = [0,1,2,1,2,0,1]

print("\nOriginal List:")
print(nums)
print(see_sum(nums,4)) #test for first 4 elements if total is 4
print(see_sum(nums,3)) #test for first 3 elements if total is 3
print(see_sum(nums,6)) #test for first 6 elements if total is 6
print(see_sum(nums,7)) #test for first 7 elements if total is 7

