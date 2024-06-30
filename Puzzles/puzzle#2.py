#Write a Python program that accepts a list of integers and calculates the length and the fifth element. 
#Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
def CheckList(user_list):
    fifth_element = 0

    for i in range(len(user_list)):
        if user_list[i] == user_list[4]: #This compares all elements in the list if it is the same with the 5th element
            fifth_element += 1

    if len(user_list) == 8 and fifth_element == 3: #Conditions for the problem
            return True
    else:
            return False
        

user_list=[]

user_input = input("Enter list of integer. Separate each number by a comma: ")
InitialList = user_input.split(",")
user_list = InitialList

#INPUT TEST CASES
#19,19,15,5,5,5,1,2 # TRUE 
#19,15,5,7,5,5,2 # FALSE
#11,12,14,13,14,13,15,14 # TRUE
#19,15,11,7,5,6,2 #FALSE

print(CheckList(user_list))

