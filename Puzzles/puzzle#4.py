#We are making n stone piles! The first pile has n stones. 
# If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. 
# Each pile must more stones than the previous pile but as few as possible. 
# Write a Python program to find the number of stones in each pile.

        
pile =[]
piles = int(input("Enter a number: "))
pile.append(piles)      #insert the input as index 0 

for i in range(piles-1): 

    if len(pile) > piles: #stops the iteration when the # of elements exceeds the input
        break

    if pile[0] % 2 == 0 or pile[0] % 2 == 1:
        piles += 2 
        pile.append(piles)


print(pile)
#TEST CASES
#Input: 2 [2, 4]
#Input: 10 [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
#Input: 3 [3, 5, 7]
#Input: 17 [17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

    
    













