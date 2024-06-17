def square(Number):
    return Number * Number

Number = int(input("What number would you like to square? "))

squared = square(Number)

print("The squared value of " + str(Number) + " is " + str(squared) + ".")