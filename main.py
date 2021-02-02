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

game_images = [rock, paper, scissors]
user_input = input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
user_choice = int(user_input)

if user_choice > 2 or user_choice < 0:
  print("I could'nt understand, please replay")
else:
  print(game_images[user_choice])

  computer_choice = random.randint(0, 2)
  print(f"Computer chose: {computer_choice}")
  print(game_images[computer_choice])

  if user_choice == computer_choice:
    print("Nobody losed, nobody win, it's a draw")
  elif user_choice == 0 and computer_choice == 1:
    print("Computer win")
  elif user_choice == 0 and computer_choice == 2:
    print("You win")
  elif user_choice == 1 and computer_choice == 0:
    print("You win")
  elif user_choice == 1 and computer_choice == 2:
    print("Computer win")
  elif user_choice == 2 and computer_choice == 0: 
    print("Computer win")
  elif user_choice == 2 and computer_choice == 1:
    print("You win")
