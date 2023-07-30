import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock, paper, scissors]


#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or @ for Scissors.\n"))
print(game_img[user_choice])


computer_choice = random.randint(0,2)
print("Computer chose :")
print(game_img[computer_choice])


#condition:
    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.


#condition
if  user_choice >= 3 or user_choice < 0:
    print("You chose an invalid number. You lose")
elif user_choice == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print("You Lose") 
elif computer_choice > user_choice:
    print("You Lose")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's a draw")
elif  user_choice >= 3 or user_choice <= 0:
    print("You chose an invalid number. You lose")
