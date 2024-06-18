#OOP Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
#=============================================

class vehicle1:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

Tesla = vehicle1("260kph", "30,000km")
print(Tesla.max_speed,Tesla.mileage)

#OOP exercise 2 Create a Vehicle class without any variables and methods
#===========================================================================

class vehicle2:
    #Class body
    pass


#OOP exercise 3 Create a child class Bus that will inherit all of the variables and methods of the Vehicle class. Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.=============================================================================
class vehicle3:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class bus3(vehicle3):
    pass

ChildBus = bus3("School bus", "260kph"," 30,000km")
print("Vehicle name: " + ChildBus.name + ", Speed: "+ ChildBus.max_speed + ", Mileage: " + ChildBus.mileage)

#OOP exercise 4. Class inheritance 
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.==============================================================================
class Vehicle4:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
class Bus4(Vehicle4):
        def seating_capacity(self,capacity=50):
            return super().seating_capacity(capacity=50)
        pass

ChildBus1 = Bus4("Yellow","50kph","30,000km")
print(ChildBus1.seating_capacity())

#OOP OOP Exercise 5: Define a property that must have the same value for every class instance (object). 
# -Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
# ====================================================================

class Vehicle5:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = "White"

    def paint_color(self):
        print("Color: " + self.color + ", Vehicle name: " + self.name + ", Speed: " + str(self.max_speed) +", Mileage: " + str(self.mileage))
        #Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18


        
class Bus5(Vehicle5):
    pass

class Car5(Vehicle5):
    pass

SchoolBus5 = Bus5("School Volvo",180,12,)
Scar5 = Car5("Audi Q5", 240, 18)

Scar5.paint_color()
SchoolBus5.paint_color()

#OOP exercise 6 Class Inheritance
#Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

#Note: The bus seating capacity is 50. so the final fare amount should be 5500. You #need to override the fare() method of a Vehicle class in Bus class.  ====================================================================

class Vehicle6:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus6(Vehicle6):
        def fare(self,capacity=50): #OVERRIDES PARENT'S FARE FUNCTIONS 
            base_fare = super().fare() #calculates fare for 50 people based on Parent's fare formula
            maintenance = base_fare * 0.10 #10% maintenance for buses
            total = base_fare + maintenance #total fare for bus with 50 seats
            return total
        pass

School_bus6 = Bus6("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus6.fare())

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