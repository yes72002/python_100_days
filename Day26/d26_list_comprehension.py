numbers = [1, 2, 3]

# numbers + 1
# for loop
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
# List Comprehension
# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
print(new_list)

# string
name = "Angela"
letters = [letter for letter in name]
print(letters) # list ['A', 'n', 'g', 'e', 'l', 'a']

# all python sequences is available
# list, range, string, tuple

# challenge: double range
new_range = [n*2 for n in range(1, 5)]
print(new_range)

# Congitional List Comprehension
# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) == 4]
print(short_names)
# challenge: uppercase names
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)




