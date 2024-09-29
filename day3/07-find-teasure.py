print('''
*******************************************************************************
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
*******************************************************************************
''')

print("Welcome to the teasure Island!")
print("Your Mission is to find the treasure!")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "Left" or "Right"?').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake, '
          'there is an island in the middle of the lake. '
          'Type "wait" to wait for a boat. '
          'Type "swim" to swim across the lake.').lower()
    if choice2 == "wait":
        choice3 = input("You Arrived at the island unharmed"
                        "There is house with 3 doors. One Red"
                        "One yellod and one blue. "
                        "Which clolour do you choose?").lower()
        if choice3 == "red":
            print("You have found the fire room, GAME OVER!")
        elif choice3 == "yellod":
            print("You have found the treasure! CONGRATULATIONS!")
        elif choice3 == "blue":
            print("You have found roof of beast, GAME OVER!")
        else:
            print("You chose a door that doesn't exist, GAME OVER!")
    else:
        print("You are eating by the crocodile, GAME OVER!")
else:
    print("You fell in to a hole. Game Over!")
