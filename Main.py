#GLOBAL VARIABLE
#y = "world"

#GLOBAL KEYWORD
#def say():
    #print(y)

#LOCAL VARIABLE 
#def sayHello():
   # x = "Hello"
    #print(x)
   # print(y)

#sayHello()

#PARAMETER VARIABLE
#def say(word):
    #print(word)
################################################################

#Imports functions from Arithmetic file
#File + "As" + declarion helps us shorten imported file names for easier coding

import Arithmetic as Ar 
from Arithmetic import add  #"From" keyword allows us to use the add function directly in this file


#Imports functions from Constants file
import Constants as Cs

#Imports Class objects from Objects file
import Objects as Obj

print(Ar.multiply(7,5))
print(Cs.pi)

Student1 = Obj.student("Cade", "BSIT")
Student1.introduce()
Student2 = Obj.student("Reilly", "BSCS")
Student1.introduce()