# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_float = float(height)
weight_float = float(weight)
BMI_float = weight_float / (height_float ** 2)
BMI_str = str(BMI_float)
print(BMI_str[0:1])

