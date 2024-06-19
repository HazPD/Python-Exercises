import math


#OOP 1 program to create a class representing a Circle. Include methods to calculate its area and perimeter.
#Area formula is A= pi*r2
#Perimeter formula is P=2piR
class Circle1:
    def __init__(self, radius):
        self.radius = radiusInput

    def area(self):                             #Function to calculate area
        return math.pi * self.radius ** 2
        
    def perimeter(self):                        #Funtion to calculate perimeter
        return 2 * math.pi * self.radius
    
radiusInput = float(input("Enter radius: "))    #Input for Circle Radius

obj1 = Circle1(radiusInput)                     #Object 

area1 = obj1.area()                             #Object input with be calculated of the operations within the called function

perimeter1 = obj1.perimeter()                   #Object input with be calculated of the operations within the called function

print("The area of a circle is", area1) 
print("The perimeter of a circle are", perimeter1)






    

    