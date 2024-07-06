#Write a Python program to find x that minimizes the mean squared deviation from a given list of numbers.
def mean(int_list):
    Total_Sum = 0 
    
    for i in range(len(int_list)):
        Length = len(int_list)
        Total_Sum += int_list[i]
        mean = Total_Sum / Length
    return mean

int_list = [4, -5, 17, -9, 14, 108, -9]
print(mean(int_list))














#Input:
#[4, -5, 17, -9, 14, 108, -9]
#Output:
#17.142857142857142