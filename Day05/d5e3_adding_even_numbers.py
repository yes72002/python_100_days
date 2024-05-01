#Write your code below this row 👇
# method 1
total = 0
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# method 2
total = 0
for number in range(2, 101, 2):
    total += number
print(total)