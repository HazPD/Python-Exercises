#class player:
   # def __init__(self,name,age):
       # self.name = name
       # self.age = age
       # print(self.name + " created")


#p1 = player("Ian","26")
#p2 = player("Cade","6")
#p3 = player("Eliz","25")

#ListOfPlayers = [p1,p2,p3]

#for i in range(len(ListOfPlayers)):
    #print(ListOfPlayers[i].name)

#################################################################################

class Player:
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print("Hi I'm " + self.name)

#Empty list for object input
ListOfPlayers =[]
#Loop for object input to be added on list
for i in range(2):
    name = input("Enter name: ")
    p = Player(name)    
    ListOfPlayers.append(p)

#will fetch names from the appended list and display them
for Player in ListOfPlayers:
    Player.introduce()
    