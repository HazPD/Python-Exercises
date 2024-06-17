class student:
    def __init__(self,name,course):
        self.name = name
        self.course = course

    def introduce(self):
        print("I am " + self.name + " ,a " + self.course + " student.")