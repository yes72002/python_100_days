# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1 + name2
name_low = name.lower()

name_t = name_low.count("t")
name_r = name_low.count("r")
name_u = name_low.count("u")
name_e = name_low.count("e")
name_l = name_low.count("l")
name_o = name_low.count("o")
name_v = name_low.count("v")
name_e = name_low.count("e")
# print(str(name1_t))
name_true = name_t + name_r + name_u + name_e
name_love = name_l + name_o + name_v + name_e
score = name_true * 10 + name_love
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")