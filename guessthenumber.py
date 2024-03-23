import time
import random

number = random.randint(1, 200)  # pick the number between 1 and 200

print(number)


def intro():
    print("Enter your name?")  # asks for the name
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    print("Go ahead. Guess!")


def pick():
    guessesTaken = 0
    while guessesTaken < 6:  # if the number of guesses is less than 6
        enter = input("Guess: ")  # inserts the place to enter guess
        try:  # check if a number was entered
            guess = int(enter)  # stores the guess as an integer instead of a string
            if guess <= 200 and guess >= 1:  # if they are in range
                guessesTaken = guessesTaken + 1  # adds one guess each time the player is wrong
                if guessesTaken < 6:
                    if guess > number:
                        print("Oops your guess is too high")
                    if guess < number:
                        print("Oops your guess is too low")
                    if guess != number:
                        print("Try again!")
                if guess == number:
                    break  # if the guess is right, then we are going to jump out of the while block

            if guess > 200 or guess < 1:  # if they aren't in the range
                print("Silly Goose! That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number in the range")
        except:  # if a number wasn't entered
            print("I don't think "+enter+" is a number sorry")
    if guess == number:
        guessesTaken = str(guessesTaken)
        print(f"good job {name}, you have found the right number in {guessesTaken} guesses!")
    if guess != number:
        print(f"Nope, the number i was thinking of was {number}")


playagain = "yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes":
    intro()
    pick()
    print("Do you want to play again")
    playagain = input()
