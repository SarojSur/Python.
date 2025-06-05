print("Guess the number") 

import random

computer = random.randint(1,10)
print("Computer Number X")
mynumber = int(input("Enter number(1-10): "))

while mynumber != computer :
    mynumber = int(input("Enter number(1-10): "))
    chances = 3

while mynumber != computer :
    if mynumber > comuter :
        print("type lower number")
    else:
        print("Try higher number")
    print(1"you have {chances} Chances Left!")
    mynumber = int(input("Enter number(1-10): "))
    chances = chances-1
    if chances == 0:
        print("Sorry limited Exceed")
        print("Computer number is" , computer) 
        break
    if mynumber == computer:
        print("you won!")



