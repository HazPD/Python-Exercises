#Write a Python program to find the largest k numbers from a given list of numbers.
def GoFind(SortedList):
    KCounter = 0
    KList = []
    for i,j in enumerate(SortedList):
        if SortedList[i] >=  SortedList[i+1]:
            KList.append(j)
            KCounter += 1

        if KCounter == K:
            break

    return KList
            
int_list = [1, 2, 3, 4, 5, 5, 3, 6, 2]
SortedList = int_list.sort(reverse = True)
K = int(input("Enter N of max numbers you want: "))
print(GoFind(int_list))