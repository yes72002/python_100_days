# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI_float = weight / (height ** 2)
BMI = round(BMI_float)

if BMI_float < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI_float < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI_float < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI_float < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")