import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []
for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

print(password_list)
password = ""
random.shuffle(password_list)
for char in password_list:
    password += char
print(password)

# CHALLENGE 2
""" for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
 """

# CHALLENGE 1
""" 
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65]
total_exam_score = sum(
    student_scores
)  # listelerde dahil olmak üzere herhangi bir yinelenebilir veri türünü koymamıza izin verir.
#print(total_exam_score)
#print(max(student_scores))

#max
max_score=0
for score in student_scores:
    if score >max_score:
        max_score=score
print(max_score)

#sum
sum = 0
for score in student_scores:
    sum += score
print(sum)
 """
