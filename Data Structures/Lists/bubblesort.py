my_list = [8, 10, 6, 2, 4]  # list to sort

swap = True

while swap:
    swap = False
    for i in range(len(my_list) -1 ):  # we need (5 - 1) comparisons
        #current index to be compared to the next index
        if my_list[i] > my_list[i + 1]:  # compare adjacent elements
            swap = True
        #if true, it will swap the current index being compared to the next one
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 

print(my_list)