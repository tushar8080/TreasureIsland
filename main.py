print('''*******************************************************************************
         |                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
         |                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
         |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')


print("\t\tWelcome to the Treasure Island\n\n")
print("Your mission is to find the treasure.")
choice_1 = input("You are at a crossroad. Where do you want to go? Type 'Left' or 'Right'\n").lower()
if choice_1 == "left":
    choice_2 = input("What do you want to do now, you have two option!!!! 'WAIT' for the boat OR 'SWIM'"
                     " to the island\n").lower()
    if choice_2 == "wait":
        choice_3 = input("You reached the Island unharmed. There is a house with three doors. One red ,one yellow and"
                         " one green. Which one do you choose?\n").lower()
        if choice_3 == "yellow":
            print("YOU WON HURRAY!!!ALL YOURS NOW")
        else:
            print("GAME OVER")
    else:
        print("Crocodile caught you. GAME OVER")
elif choice_1 == "right":
    print("SORRY!! You fell into a Hole. GAME OVER")
