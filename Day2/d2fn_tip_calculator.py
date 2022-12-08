#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")

total_bill_float = float(input("What was the total bill? $"))
percentage_float = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_int = int(input("How many people to split the bill? "))
total_pay = total_bill_float * (1 + percentage_float/100)
each_pay = (total_pay / people_int)
# print(str(each_pay))
# round method 1
each_pay_round1 = round(each_pay, 2)
# round method 2, solve bill 150, percentage 12, people 5, output 33.6 problem
# turn eachpay form float into string and then take the first two bits after the dot
each_pay_round2 = "{:.2f}".format(each_pay)
each_pay_round3 = str(round(each_pay ,2)) # didn't work

print(f"Each person should pay: ${each_pay_round1}")
print(f"Each person should pay: ${each_pay_round2}")
print(f"Each person should pay: ${each_pay_round3}")
