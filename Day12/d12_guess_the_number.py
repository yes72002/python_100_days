#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo


def game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = random.randint(1,101)
  print(f"Passt, the correct answer is {answer}")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  # difficulty = "easy"
  # difficulty = "hard"
  if difficulty == "easy":
    chance = 10
  else:
    chance = 5
  
  guess = 0
  while guess != answer:
    print(f"You have {chance} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == answer:
      print(f"You got it! The answer is {answer}")
    else:
      if guess > answer:
        print("Too high.")
      else:
        print("Too low.")
      chance -= 1
      if chance == 0:
        print("You've run out of guesses, you lose.")
        return
      else:
        print("Guess again.")

game()