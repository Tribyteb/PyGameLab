import random
import time

playGame = input("Wanna Play Number Guess Game? ( Y / N )")
while (playGame == "Y"):
    guessChance = 7
    randomNumber = random.randint(1,100)

    while True:
        guessNumber = int(input("Guess The Number (1-100):"))

        if (guessNumber < randomNumber):
            print("Calculating...")
            time.sleep(2)
            print("Number is higher than your guess")
            guessChance -= 1

        elif (guessNumber > randomNumber):
            print("Calculating...")
            time.sleep(2)
            print("The number is lower than your guess")
            guessChance -= 1

        else:
            print("Calculating")
            time.sleep(1)
            print("You Won! Correct Number is", randomNumber)
            break

        if (guessChance == 0):
            print("You Lost! Correct Number is", randomNumber)
    playGame = input("Do you want to play again ? :")

        
else:
    print("Game End...")
