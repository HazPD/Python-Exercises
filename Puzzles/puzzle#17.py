#Write a Python program to create a string consisting of non-negative integers up to n inclusive.
def go_run(number):
    int_list = " "
    for i in range(number + 1):
        if i > number:
            break
        else:
            int_list += str(i)              
            int_list += " "
            
    return int_list

number =  int(input("Enter number: "))

print(go_run(number))

#NOTES 
#Adding stuff on list and emptry strings are two different things