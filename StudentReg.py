class Student:
    #Used constructor
    def __init__(self,StudentNumber,Name,Course,Year,Section):
        self.StudentNumber = StudentNumber
        self.Name = Name
        self.Course = Course
        self.Year = Year
        self.Section = Section
    #Function for output
    def introduce(self):
        print(self.StudentNumber)
        print(" -" + self.Name)
        print(" -" + self.Course)
        print(" -" + self.Year)
        print(" -" + self.Section)
           


#Made empty list for input       
Registrar = []

#String based while loop for possible multiple data entry
while True : 
    answer = input("Would you like to enroll a student? Yes/No? ")
    if answer == 'Yes':
        
            StudentNumber = str(input("Student number: "))
            Name = str(input("Enter name: "))
            Course = str(input("What is your course? "))
            Year = str(input("What year are you in? "))
            Section = str(input("Choose your section? "))

            #object for new enrollee
            new_student = Student(StudentNumber,Name,Course,Year,Section)
            
            #Will add new input to the list
            Registrar.append(new_student)

            print(Name + " has been enrolled.")
            print("--------------------")
            
    elif answer == 'No':
         print("Thank you for enrolling students.")
         break
    
    else:   
        print("Invalid Answer")
        

for new in Registrar:
    new.introduce()




    

    

