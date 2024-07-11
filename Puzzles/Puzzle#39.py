#Write a Python program to determine which triples sum to zero from a given list of lists.
def check(int_list):
    Bool = []
    
    for i in int_list:
        x = sum((item) for item in i)
        if x == 0: 
            Bool.append("True")
        else:
            Bool.append("False")
    return Bool
int_list = [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]]

#TEST CASES
# [[1, 2, -3], [-4, 0, 4], [0, 1, -5], [1, 1, 1], [-2, 4, -1]] = [True, True, False, False, False]

print(check(int_list))