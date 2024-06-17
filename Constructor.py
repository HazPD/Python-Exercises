class character:
    def __init__(self,ign,hp,stamina,atk,lvl):
        self.ign = ign
        self.hp = hp
        self.stamina = stamina
        self.atk = atk
        self.lvl = lvl
        print("Character " + ign + " Created")

charOne = character("Haz","100","50","1","1")
charTwo = character("Wapol bading","1","1","1","1")