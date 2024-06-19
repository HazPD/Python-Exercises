from datetime import date 

#OOP 2 EXERCISE Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age. 
#=================================================================================
class person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob

    def calculate_age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(self.dob.year, self.dob.month, self.dob.day):
            age += 1 
        return age
    
person1 = person("wapol", "Afghanistan",date(2001,11,26))
person2 = person("aru", "China",date(2002,12,5))
person3 = person("haz", "India",date(1998, 10, 14))

print("Person 1")
print("My name is " + person1.name)
print("I'm from" + person1.country)
print("I was born on " + str(person1.dob))
print(person1.calculate_age())

print("Person 2")
print("My name is " + person2.name)
print("I'm from" + person2.country)
print("I was born on " + str(person2.dob))
print(person2.calculate_age())

print("Person 3")
print("My name is " + person3.name)
print("I'm from" + person3.country)
print("I was born on " + str(person3.dob))
print(person1.calculate_age())