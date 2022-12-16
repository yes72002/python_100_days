# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# method 1
# print((names))
# length = len(names)
# i = random.randint(0, length-1)
# print(names[i] + " is going to buy the meal today!")

# method 2
person = random.choice(names)
print(person + " is going to buy the meal today!")