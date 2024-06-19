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