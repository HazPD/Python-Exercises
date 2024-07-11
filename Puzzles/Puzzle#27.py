#Write a Python program to find x that minimizes the mean squared deviation from a given list of numbers.
def mean(int_list):
    Total_Sum = 0 
    
    for i in range(len(int_list)):
        Length = len(int_list) #declaration of length of list
        Total_Sum += int_list[i] #addition of all elements
        mean = Total_Sum / Length #Divides the sum by # of elements in list
    return mean

int_list = [4, -5, 17, -9, 14, 108, -9]
print(mean(int_list))

#Input:
#[4, -5, 17, -9, 14, 108, -9]
#Output:
#17.142857142857142