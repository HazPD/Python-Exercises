#Write a Python program to find the sum of the numbers in a given list among the first k with more than 2 digits.
def Kfunc(int_list):
    Hundred = []
    KSum = 0
    Kcounter = 0
    for i in int_list:
        if len(str(i)) > 2:
            Hundred.append(i)
            Kcounter += 1
            
        if Kcounter == K:
            break
    
    for i in Hundred:
        KSum += i
    
    return KSum
        
int_list = [4, 5, 17, 9, 143, 108, -9, 12, 76]
K = 6

print(Kfunc(int_list))