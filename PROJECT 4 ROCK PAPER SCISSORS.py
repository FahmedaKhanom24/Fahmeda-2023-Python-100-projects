# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
import random
Rock= ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

Paper= ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

Scissors= ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
#map = [Rock, Paper, Scissors]


game_images = [ Rock, Paper, Scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors.\n"))

if user_choice < 0 or user_choice >=3:
    print("You typed an invalid number. You lose!") 


else:
    print(game_images[user_choice])
    computer_choice = random.randint(0,2)
    print(f"Computer Choose: {computer_choice}")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice ==0 and computer_choice==2:
        print("You win")
    elif user_choice==2 and computer_choice==0:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif user_choice < computer_choice:
        print("You lose")



