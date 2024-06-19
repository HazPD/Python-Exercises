#OOP Exercise 7: Check type of an object
#Write a program to determine which class a given Bus object belongs to. 

class Vehicle7:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus7(Vehicle7):
    pass

School_bus7 = Bus7("School Volvo", 12, 50)
print(type(School_bus7)) 