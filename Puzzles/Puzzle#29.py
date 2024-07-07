#Write a Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
def zero(int_list):
    location = []
    Sum = 0
    for i, v in enumerate(int_list):
        for j in int_list:
            if j + v == Sum:
                location.append(i)
    return location

int_list = [1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
#TEST CASES
#[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20] [1,7]
#[1, -4, 6, 7, 4] - [1,4]
print(zero(int_list))
