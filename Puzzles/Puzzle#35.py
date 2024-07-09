#Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any.
def multiple(Nums2):
    Odd = []
    Product = 1
    
    for i in Nums2:
        if i % 2 == 1:
            Odd.append(i)

    for i in Odd:
        Product *= i

    if Odd == []:
        return 0
    
    return Product


Nums = int(input("Enter number: "))
Nums2 = [int(char) for char in list(str(Nums))]

print(multiple(Nums2))