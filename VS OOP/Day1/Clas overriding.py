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