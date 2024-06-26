# Collatz Conjecture idea into while loop
#(if even, divide by two; if odd, triple it and add one)
steps = 0
print("Collatz Conjecture")
StartingNum = int(input("Enter a number: "))

if StartingNum < 1:
    print("Negative integers doesn't work for the Conjecture ")

while StartingNum != 1:
    if StartingNum % 2 == 0:
        StartingNum = StartingNum / 2
        print(StartingNum)
        steps = steps + 1
    else:
        StartingNum %2 == 1
        StartingNum = (StartingNum * 3) + 1
        print(StartingNum)
        steps = steps + 1
print("Total steps: ",steps)
