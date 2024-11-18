print(
    '''
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
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************''',
    "\nWelcome to Treasure Island.\nYour mission is to find the treasure.\nYou're at a cross road. Where do you want to go?",
    '\n\t Type "left" or "right"',
)
direction = input().lower()
if direction == "left":
    print(
        """You've come to a lake. There is an island in the middle of the lake.\n\tType "wait" to wait for a boat. Type "swim" to swim across."""
    )
    wait = input().lower()
    if wait == "wait":
        print(
            """You arrive at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?"""
        )
        door = input().lower()
        if door == "yellow":
            print("You Win!")
        elif door == "red":
            print("Burned by fire.\nGame Over.")
        elif door == "blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout.\nGame Over")
else:
    print("Fall into a hole.\nGame Over.")