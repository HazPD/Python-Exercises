class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return self.num1 / self.num2
    
num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

addition = calculator(num1, num2)
subrtraction = calculator(num1, num2)
multiplication = calculator(num1, num2)
division = calculator(num1, num2)

sum = addition.add()
difference = subrtraction.subtract()
product =  multiplication.multiply()
quotient = division.divide()


print("The sum is: ", sum)
print("The difference is: ", difference)
print("The product is: ", product)
print("The quotient is: ", quotient)

    