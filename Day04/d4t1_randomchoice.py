# Python random Module – Generate Random Numbers/Sequences
# https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences
# from 2. random.choice()
import random
 
a = ['one', 'eleven', 'twelve', 'five', 'six', 'ten']
 
print(a)
 
for i in range(5):
    print(random.choice(a))