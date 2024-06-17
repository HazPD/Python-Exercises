Tries = 3


while Tries > 0:
    guess = int(input("What is 50 divided by 5? "))
    if guess == 10:
        print("You're right! 50 divided by 5 is 10")
        #Ends the game
        break
    else:
        #reduction of tries for every wrong answer
        Tries = Tries - 1
        print("Incorrect!, You have " + str(Tries) + " tries left")
    if Tries == 0:
                print("Game over")
                #Ends the game
                break
    

        
    

