import random

print("Welcome to rook, paper, sizer game")
choices = ["Rock","Paper","Scissor"]

computer = random.choice(choices)
my_choice = input("Enter your choice: ")

'if' (my_choice == "Rock" and computer == "Scissor"):
print("You Won")
print("Computer Choose: ",computer)

elif (my_choice == "Scissor" and computer == "Rock"):
print("You loss")
print("Computer Choose: ",computer)

elif (my_choice == "Paper" and computer == "Rock"):
print("You Won")
print("Computer Choose: ",computer)

elif (my_choice == "Paper" and computer == "Scissor"):
print("You loss")
print("Computer Choose: ",computer)

else:
    if (my_choice == "Scissor" and computer == "paper"):
print("You Won")
print("Computer Choose: ",computer)

