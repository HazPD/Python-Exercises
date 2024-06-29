#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615

n = str(input("Enter a number: "))
n2 = n + n 
n3 = n + n + n 
result = int(n) + int(n2) + int(n3)

print(result)

