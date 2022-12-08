# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# 90 years
# 90 * 365 = 32850 days
# 90 * 52 = 4680 weeks
# 90 * 12 = 1080 months
age_int = int(age)
year_left = 90 - age_int
# print(90 * 365 - age_int * 365)
# print(90 * 52 - age_int * 52)
# print(90 * 12 - age_int * 12)
day_left = (year_left * 365)
week_left = (year_left * 52)
month_left = (year_left * 12)
print(f"You have {day_left} days, {week_left} weeks, and {month_left} months left.")



