import math


#OOP 4 program to create a class representing a Circle. Include methods to calculate its area and perimeter.
#Area formula is A= pi*r2
#Perimeter formula is P=2piR
class Circle1:
    def __init__(self, radius):
        self.radius = radiusInput

    def area(self):                             #Function to calculate area
        return math.pi * self.radius ** 2
        
    def perimeter(self):                        #Funtion to calculate perimeter
        return 2 * math.pi * self.radius
    

class Triangle:
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def TArea(self):
        return  1/2 * self.base * self.height

    def TPerimeter(self):
        return AreaOfTriangle + self.base + self.height
    


#CIRCLE FUNCTIONS    
radiusInput = float(input("Enter radius: "))    #Input for shape Radius

obj1 = Circle1(radiusInput)                 

area1 = obj1.area()                             #Object input with be calculated of the operations within the called function

perimeter1 = obj1.perimeter()                   #Object input with be calculated of the operations within the called function

print("The area of a circle is", area1) 
print("The perimeter of a circle are", perimeter1)

#TRIANGLE FUNCTIONS

TbaseInput = float(input("Enter base: "))
TheightInput = float(input("Enter height: "))

#declation on input parameters
obj2 = Triangle(TbaseInput,TheightInput)

AreaOfTriangle = obj2.TArea()

PerimeterOfTriangle = obj2.TPerimeter()

print("The area of a triangle is", AreaOfTriangle) #6.5
print("The perimeter of a triangle is", PerimeterOfTriangle) #12.5

#SQUARE FUNCTION 
class square:
    def __init__(self,side):
        self.side = side

    def SArea(self):
        return self.side * self.side
    
    def Sperimeter(self):
        return self.side * 4
    
SideInput = int(input("Enter side: "))

obj3 = square(SideInput)

AreaOfSquare = obj3.SArea()
PerimeterOfSquare = obj3.Sperimeter()

print("The area of a square is ", AreaOfSquare)
print("The perimeter of square is ",PerimeterOfSquare)


