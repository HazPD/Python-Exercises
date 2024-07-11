# Write a Python program to find the largest integer divisor of a number n that is less than n.


def divisor(nums):
    x = nums / 2
    return x

nums = int(input("Enter a number: "))
print(divisor(nums))