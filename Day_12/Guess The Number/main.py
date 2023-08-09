import random
import os
from art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

#Make function to set difficulty.
def difficulty():
    level = input("Chose a difficulty. Type 'easy' or 'hard' : ").lower()
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

turns = 0
#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too Low.")
        return turns - 1
    else:
        print(f"You got it! The random number was : {answer}")


#game
def game():
    print(logo)
    #Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")      
    answer = random.randint(1,100)

    turns = difficulty()
    
    guess =0
    while guess != answer:
        #let guess a number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()

while input("Do you wanna play game again? Type 'y' or 'n' : ") == "y":
    os.system("cls")
    game()