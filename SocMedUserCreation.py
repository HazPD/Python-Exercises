class user:
    def __init__(self,firstName,lastName,likesCount,friends):
        self.fn = firstName
        self.ln = lastName
        self.lc = likesCount
        self.fl = friends
        self.FL = firstName + " " + lastName

    def introduce(self):
        print("Hi, I'm " + self.FL)

    def fullProfile(self):
        print("Full name: " + self.FL)
        print("Likes: " + self.lc) 
        for i in range(len(self.fl)):
            print(" -" + self.fl[i])

User1 = user("Haz","Panen","25",friends =["Alenere Sdpt","Jaymar Catapang","Joshua Emmanuel Seria","Patrick Macaraig"]) 
User1.introduce()
User1.fullProfile()
