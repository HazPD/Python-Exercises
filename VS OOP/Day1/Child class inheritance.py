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