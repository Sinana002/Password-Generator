#hard level password generator

import string
import random
letters = list(string.ascii_letters)  # a-z + A-Z
numbers = list(string.digits)         # 0-9
symbols = list('!@#$%^&*()-_=+[]{}|;:,.<>?/~`')

print("Welcome to my password generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list=[]

for char in range(1,nr_letters+1):
  password_list.append(random.choice(letters))
  #print(password)
for char in range(1,nr_symbols+1):
  password_list.append(random.choice(symbols))
for char in range(1,nr_numbers+1):
  password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
print(password_list)

password=""
for char in password_list:
  password=password+char
print(f'your password is:{password}')
