#Write a Python program to find the indices at which the numbers in the list drop.
#Note: You can detect multiple drops just by checking if nums[i] < nums[i-1]

def CheckDrop(Int_List):
    indeces = []
    for i,value in enumerate(Int_List):
        if Int_List[i] < Int_List[i-1]:
            indeces.append(i)
    return indeces
    
Int_List = [6, 5, 4, 3, 2, 1]
print(CheckDrop(Int_List))

#TEST CASES 
#[0, -1, 3, 8, 5, 9, 8, 14, 2, 4, 3, -10, 10, 17, 41, 22, -4, -4, -15, 0] = [1, 4, 6, 8, 10, 11, 15, 16, 18]
#[6, 5, 4, 3, 2, 1] = [1, 2, 3, 4, 5]
#[1, 19, 5, 15, 5, 25, 5] = [0, 2, 4, 6]