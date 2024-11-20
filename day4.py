# DAY4 FINISH
import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]

user_choose = int(
    input("What do you choose? Type 0 for Rock, 1 Paper or 2 for Scissors.")
)
if user_choose >= 0 and user_choose <= 2:
    print(f" Your Chose\n{game_images[user_choose]}")
    computer_choose = random.randint(0, 2)
    print(f"Computer Chose\n{game_images[computer_choose]}")
if user_choose >= 3 or user_choose < 0:
    print("You typed an invalid number. You lose!")
elif user_choose == 0 and computer_choose == 2:
    print("You Win")
elif computer_choose == 0 and user_choose == 2:
    print("You Lose")
elif computer_choose > user_choose:
    print("You Lose")
elif user_choose > computer_choose:
    print("You Win")
elif computer_choose == user_choose:
    print("It's draw!")

# benim çözümüm
""" 
#girdi alma
user_choose = int(
    input("What do you choose? Type 0 for Rock, 1 Paper or 2 for Scissors.")
)
#seçimi bastırma
print("Your Choice:")
if user_choose == 0:
    print(rock)
elif user_choose == 1:
    print(paper)
elif user_choose == 2:
    print(scissors)

#doğru girdi varsa pc seçimi üretme
if user_choose <=2:

    computer_choose = random.randint(0, 2)
    print("Computer Choice:")
    if computer_choose == 0:
        print(rock)
    elif computer_choose == 1:
        print(paper)
    elif computer_choose == 2:
        print(scissors)

#Sonuçu yazdırma
if user_choose == 0:
    if computer_choose == 0:
        print("Draw")
    elif computer_choose == 1:
        print("Lose")
    elif computer_choose == 2:
        print("Win")
elif user_choose == 1:
    if computer_choose == 0:
        print("Win")
    elif computer_choose == 1:
        print("Draw")
    elif computer_choose == 2:
        print("Lose")
elif user_choose == 2:
    if computer_choose == 0:
        print("Lose")
    elif computer_choose == 1:
        print("Win")
    elif computer_choose == 2:
        print("Draw")
else:
    print("Wrong input!")
 """

# DAY4 EXERCISE2
""" import random

friends = ["Burak", "Berk", "Batu", "Rderin", "Tugba", "Hakan"]
randomNumber = random.randint(0, len(friends) - 1)
randomPeople = random.choice(friends)  # seçilen yerden random bir elemanı döner.
print(friends[randomNumber])
print(randomPeople)
 """

# DAY4 EXERCISE1
""" import random

a = random.randint(1, 10)#başlangıç ve bitiş değeri dahildir.
b = random.randrange(start=0, stop=17, step=3)#belli bir range aralığı verip sonuncu dahil değil
c=random.random()#0-1 arasında float random bir sayı üretir 1 dahil değildir.
d=random.uniform(1,10) #verdiğimiz aralıkta bir sayı üretir bitiş değeride dahildir.
print(a)
print(b)
print(c)
print(d)
 """
