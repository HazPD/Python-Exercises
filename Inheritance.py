class parent:
    def __init__(self,firstname,lastname,age):
        self.fn = firstname
        self.ln = lastname
        self.age = age
    
    def introduce(self):
        print("Hi! My name is " + self.fn)
        print()

class child(parent):
        def __init__(self, firstname, lastname, age,bday,school):
             super().__init__(firstname, lastname, age)
             self.bday = bday
             self.school = school
        pass
        
        def details(self):
             super().introduce()
             print("I was born " + self.bday + "and I study at " + self.school)

charOne = parent("Haz","Nenap","26")
charOne.introduce()
chartwo = child("Cade", "eryx", "6","12-03-17","Hillcrest")
chartwo.details()