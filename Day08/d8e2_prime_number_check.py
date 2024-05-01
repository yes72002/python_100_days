#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    if number == 1:
        print("It's not a prime number.")
    elif number == 2:
        print("It's a prime number.")
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
# print(7 % 1)
# print(7 % 2)
# print(7 % 7)
#Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

# check from 1 to 100
# for n in range(1, 101):
    # prime_checker(number=n)