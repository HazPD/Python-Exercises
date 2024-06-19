#OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class Vehicle8:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus8(Vehicle8):
    pass

School_bus8 = Bus8("School Volvo", 12, 50)
print(isinstance(School_bus8,Vehicle8))