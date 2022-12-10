import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
images = [rock, paper, scissors]
if choose >=3 or choose < 0:
  print("You typed an invalid number, you lose!")
else:
  print(images[choose])

  computer_choose = random.randint(0, 2)
  print("Computer choose: ")
  print(images[computer_choose])
  
  if computer_choose == 0:
    if choose == 0:
      print("draw")
    elif choose == 1:
      print("You win")
    else:
      print("You lose")
  elif computer_choose == 1:
    if choose == 0:
      print("You lose")
    elif choose == 1:
      print("draw")
    else:
      print("You win")
  else:
    if choose == 0:
      print("You win")
    elif choose == 1:
      print("You lose")
    else:
      print("draw")