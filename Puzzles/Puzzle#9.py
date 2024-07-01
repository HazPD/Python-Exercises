#Write a Python program to find a list of integers containing exactly four distinct values, such that no integer repeats twice consecutively among the first twenty entries.
def check(int_list):
    for i in range(len(int_list)):
        if int_list[i] != int_list[i+1] and len(unique_int) == 4:
            return True
        else:
            return False
def unique_count(unique_int):
    for i in int_list:
        if i not in unique_int:
            unique_int.append(i)

unique_int = []
int_list =[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] 

unique_count(unique_int)
print(int_list)
print("Number of unique: ",len(unique_int))
print(check(int_list))

#TEST CASES
#[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] True

#[1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3, 1, 2, 3, 3] False

#[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3] False

#[5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8, 5, 6, 7, 8] True