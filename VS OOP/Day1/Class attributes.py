#OOP Exercise 1: Create a Class with instance attributes
#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
#=============================================

class vehicle1:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

Tesla = vehicle1("260kph", "30,000km")
print(Tesla.max_speed,Tesla.mileage)