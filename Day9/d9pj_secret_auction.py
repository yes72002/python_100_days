from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the secret auction program. ")

dictionary = {}
others = "yes"

while others == "yes":  
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  dictionary[name] = bid
  # print(dictionary)
  others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  clear()

highest_bid = 0
for key in dictionary:  
  if dictionary[key] >= highest_bid:
    highest_name = key
    highest_bid = dictionary[key]

print(f"The winner is {highest_name} with a bid of {highest_bid}")