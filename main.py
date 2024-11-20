# DAY3 EXERCISE 2
total = 0
print("Welcome Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size == "S" or size == "s":
    total += 15
elif size == "M" or size == "m":
    total += 20
elif size == "L" or size == "l":
    total += 25
else:
    print("see you")
pepporoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepporoni == "Y" or pepporoni == "y":
    if size == "S" or size == "s":
        total += 2
    elif size == "M" or size == "m" or size == "L" or size == "l":
        total += 3
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y" or extra_cheese == "y":
    total += 1
print(f"Your final bill is: {total}₺")


# DAY3 EXERCISE
""" weight = 85
height = 1.85

bmi = weight / (height ** 2)

if bmi<18.5:
    print("Underweight")
elif 18.5<=bmi<25:
    print("Normal")
elif 25<=bmi :
    print("Overweight")
 """


# DAY2
"""print("Welcome the tip calculator!")
bill=float(input("What was the total bill? ₺"))
tip=int(input("How much tip would you like to give? 10, 12, or 15?"))#inte çevir
people=int(input("How many people to split the bill?"))#inte çevir
total_tip=round(tip/100,2)
tip_result= bill*total_tip
total_bill=bill+tip_result
bill_person=round(total_bill/people,2)
print(f"Each person should pay: ₺{bill_person}")"""


# DAY1
""" print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet) """
