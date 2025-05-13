'''
snake => 1
water => -1
gun => 0
'''

import random

random_number = random.choice([-1, 0, 1])

computer = random_number
youStr = input("Enter your choise: ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youStr]

reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
print(f"You choose {reverseDict[you]}\nComputer choose {reverseDict[computer]}")

if(computer == you):
    print("Game Draw!")
else:
    if(computer == -1 and you == 1):
        print("You win!")
    elif(computer == -1 and you == 0):
        print("You Loss")
    elif(computer == 1 and you == -1):
        print("You Loss")
    elif(computer == 1 and you == 0):
        print("You Win!")
    elif(computer == 0 and you == -1):
        print("You Win!")
    elif(computer == 0 and you == 1):
        print("You Loss!")
    else:
        print("Some thing went wrong!")