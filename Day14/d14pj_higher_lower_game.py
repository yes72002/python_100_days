import random
import art
from game_data import data
from replit import clear

length = len(data)

def game():
    print(art.logo)
    i = random.randint(0, length-1)
    A    = data[i]
    A_name = A["name"]
    A_follower_count = A["follower_count"]
    A_description = A["description"]
    A_country = A["country"]

    score = 0
    is_right = True

    while is_right == True:
        i = random.randint(0, length-1)
        B    = data[i]
        B_name = B["name"]
        B_follower_count = B["follower_count"]
        B_description = B["description"]
        B_country = B["country"]

        print(f"Compare A: {A_name}, {A_description}, from {A_country}")
        # print(f"{A_follower_count}")
        print(art.vs)
        print(f"Compare B: {B_name}, {B_description}, from {B_country}")
        # print(f"{B_follower_count}")

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if A_follower_count > B_follower_count:
            if guess == "A":
                is_right = True
            else:
                is_right = False
        elif A_follower_count < B_follower_count:
            if guess == "B":
                is_right = True
            else:
                is_right = False
        else:
            is_right = True

        clear()
        # print("clear")
        print(art.logo)

        if is_right == True:
            A = B
            A_name = A["name"]
            A_follower_count = A["follower_count"]
            A_description = A["description"]
            A_country = A["country"]
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            print(f"You're wrong! Current score: {score}")

game()