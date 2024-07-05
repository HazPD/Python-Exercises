#Write a Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.
def check(Input_list):
    increasing = True
    decreasing = True
    for i in range(len(Input_list)-1):
        if Input_list[i] > Input_list[i+1]:
            increasing = False
        elif Input_list[i] < Input_list[i+1]:
            decreasing = False
    
    if increasing:
        return ("Increasing")
    elif decreasing:
        return ("Decreasing")
    else:
        return ("Not a monotonic sequence")

    
Input_list = [1, 2, 3, 2, 1]
#TEST CASES12
#[1, 2, 3, 4, 5, 6]
#[6, 5, 4, 3, 2, 1]
#[19, 19, 5, 5, 5, 5, 5]
#[19, 20, 5, 5, 5, 5, 5]
#[1, 2, 3, 2, 1]
print(check(Input_list))