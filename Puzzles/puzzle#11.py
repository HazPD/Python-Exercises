# Write a Python program to find the indexes of numbers in a given list below a given threshold.

def show_index(int_list):
    indexes = []        
    thresh = 15                    
    for i,j in enumerate(int_list,0):
        if j < thresh:
            indexes.append(i)
    return indexes

int_list = [0, 12, 45, 3, 4923, 322, 105, 29, 15, 39, 55]

print(show_index(int_list))

