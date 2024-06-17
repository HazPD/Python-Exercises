class car:
    #Object constructor
    def __init__(self,unit,horn):
        self.unit = unit
        self.horn = horn
#Objection function for speak
    def speak(self):
        print(self.horn)
#Object function for unit model
    def model(self):
        print(self.unit)
#Class attributes
cOne = car("BMW", "pooot")
cOne.model()