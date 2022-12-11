#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_letter = []
password_symbol = []
password_number = []
for i in range(0, nr_letters):
  letter = random.choice(letters)
  password_letter.append(letter)
  # print(password_letter)

for i in range(0, nr_symbols):
  symbol = random.choice(symbols)
  password_symbol.append(symbol)

for i in range(0, nr_numbers):
  number = random.choice(numbers)
  password_number.append(number)

password_list = password_letter + password_symbol + password_number
# print(password_list)

# easy level
password_str = ''.join(password_list) # list to string
print(password_str)
# hard level
random.shuffle(password_list)
password_str = ''.join(password_list) # list to string
print(password_str)

# angela
password_str = ""
for char in password_list:
  password_str += char
print(password_str)