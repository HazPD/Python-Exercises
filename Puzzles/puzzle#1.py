#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. 
#Return True otherwise False.
def NumList(int_list):
        count_19 = 0
        count_5 = 0 
#Iterate through the list
        for i in range(len(int_list)):
            if int_list[i] == 19:
                count_19 += 1
            elif int_list[i] == 5:
                count_5 += 1
#conditions
        if count_19 == 2 and count_5 >= 3:
            return True
        else: 
            return False

int_list = [19, 15, 15, 5, 3, 3, 5, 2] #FALSE

#TEST CASES
#[19, 19, 15, 5, 3, 5, 5, 2] #TRUE 
#[19, 19, 5, 5, 5, 5, 5] # TRUE 
print(NumList(int_list))
