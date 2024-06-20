secret_number = 777

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop")
    guess = int(input("Guess the secret number: "))
if guess == secret_number:
    print("Well done! You managed to get out of my loop")

        