#step 1

word_list=["ardvark", "baboon", "camel"]


# TODO-1 - randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

chosen_word = random.choice(word_list)


#TODO-2 -Ask the user to gruss a letter assing their answer to a variable called guess.  Make guess lowercase.

guess = input("guess a letter: ").lower()

#TODO-3 - Check if the letter the user guessed is one of the chosen_word. 
for letter in chosen_word:
    if letter == guess:
        print("Right.")
    else:
        print("Wrong.")