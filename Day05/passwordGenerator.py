

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random
# randomLetters=''.join(random.sample(letters,nr_letters))
# random_numbers=''.join(random.sample(numbers,nr_numbers))
# random_symbols=''.join(random.sample(symbols,nr_symbols))
# password=list(randomLetters+random_symbols+random_numbers)
# random.shuffle(password)
# randomized_string=''.join(password)
# print(randomized_string)
#

password=[]
for char in range(0,nr_letters):
    password.append(random.choice(letters))
for char in range(0,nr_symbols):
    password.append(random.choice(symbols))
for char in range(0,nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(password)

passw=""
for char in password:
    passw+=char

print(f"Your password {passw}")