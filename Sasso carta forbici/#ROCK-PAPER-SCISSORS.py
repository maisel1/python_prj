#ROCK-PAPER-SCISSORS
import random

#taking player chice
player_choice = int(input("""Welcome to Rock, Paper, scissors terminal game.
      Chose:
      1) for rock;
      2) for paper
      3) for scissors
      """))
#taking computer chouce
computer_choice = random.randint(1, 3)

#printing player's and computer's selected tool
if computer_choice == 1:
    print("computer_chouce is ROCK")
elif computer_choice == 2:
    print("computer choice is PAPER")
elif computer_choice == 3:
    print("computer choice is SCISSORS")
    
if player_choice == 1:
    print("your choice is ROCK")
elif player_choice == 2:
    print("your choice is PAPER")
elif player_choice == 3:
    print("your choice is SCISSORS")
else:
    print("you chose... VIOLENCE!! (only numbers from 1 to 3 are valid)")
    
#define the winner

if computer_choice == player_choice:
    print("it's a tie")
elif computer_choice == 1 and player_choice == 2:
    print("you won!")
elif computer_choice == 1 and player_choice == 3:
    print("you lose!")
elif computer_choice == 2 and player_choice == 1:
    print("you lose!")
elif computer_choice == 2 and player_choice == 3:
    print("you won!")
elif computer_choice == 2 and player_choice == 3:
    print("you won!")
elif computer_choice == 3 and player_choice == 1:
    print("you won!")
elif computer_choice == 3 and player_choice == 2:
    print("you lose!")
else:
    print("there's something wrong")   

