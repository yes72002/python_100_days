############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
from replit import clear
import random

def calculate_score(cards_list):
  """Take a list of cards and return the score calaulated from the cards."""
  score = sum(cards_list)
  if (score == 21) and (len(cards_list) == 2):
    return 0
  elif score > 21:
    # check ace
    if 11 in cards_list:
      position = cards_list.index(11)
      cards_list[position] = 1
      # cards_list.remove(11)
      # cards_list.insert(0, 1)
      # cards_list = [1] + cards_list
    score = sum(cards_list)
    return score
  else:
    return score

def compare(score1, score2):
  if score1 > 21:
    return "You went over. You lose!"
  if score1 == score2:
    return "Draw"
  elif score2 > 21:
    return "Opponent went over. Yon win"
  elif score1 == 21:
    return "Win with a Blckdjack"
  elif score2 == 21:
    return "Yon lose"
  elif score1 > score2:
    return "Yon win"
  else:
    return "Yon lose"

def blackjack():
  print(logo)

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  your_cards = []
  for i in range(0, 2):
    card = random.choice(cards)
    # print(card)
    your_cards.append(card)
  # print(your_cards)
  # your_cards = [3, 11]
  # your_cards = [10, 11]
  deal_cards = []
  for i in range(0, 2):
    card = random.choice(cards)
    deal_cards.append(card)
  # print(deal_cards)
  # deal_cards = [10, 11]

  your_score = calculate_score(your_cards)
  deal_score = calculate_score(deal_cards)

  if your_score == 0:
    # blackjack
    print(f"   You final hand: {your_cards}, final score: 21")
    print(f"   Computer's final hand: {deal_cards}, final score: {deal_score}")
    print("You win, you have a blackjack.")
  elif deal_score == 0:  
    # blackjack
    print(f"   You final hand: {your_cards}, final score: {your_score}")
    print(f"   Computer's final hand: {deal_cards}, final score: 21")
    print("You lose, computer has a blackjack.")
  else:
    print(f"   You cards: {your_cards}, current score: {your_score}")
    print(f"   Computer's first card: {deal_cards[0]}")

    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    while get_card == "y":
      card = random.choice(cards)
      your_cards.append(card)
      
      your_score = calculate_score(your_cards)
      deal_score = calculate_score(deal_cards)
      print(f"   You cards: {your_cards}, current score: {your_score}")
      print(f"   Computer's first card: {deal_cards[0]}")
      
      if your_score > 21:
        get_card = "n"
      else:
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if your_score <= 21:
      while deal_score < 17:
        card = random.choice(cards)
        deal_cards.append(card)
        deal_score = calculate_score(deal_cards)

    print(f"   You final hand: {your_cards}, final score: {your_score}")
    print(f"   Computer's final hand: {deal_cards}, final score: {deal_score}")
    print(compare(your_score, deal_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  blackjack()