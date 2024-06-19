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