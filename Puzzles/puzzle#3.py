#Write a Python program that accepts an integer
#Determine whether it is greater than 4^4 and which is 4 mod 34.
def mod(user_input):

    if user_input > 4**4 and user_input % 34 == 4:
        return True
    else:
        return False

user_input = int(input("Enter number: "))
print(mod(user_input))

#TEST CASES
#Input: 922 True
#Input: 914 False
#Input: 854 True

