piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
#           0    1    2    3    4    5    6    7

print(piano_keys[2:5]) # ['c', 'd', 'e'], not from the second to the fifth
print(piano_keys[2:])  # ['c', 'd', 'e', 'f', 'g']
print(piano_keys[:5])  # ['a', 'b', 'c', 'd', 'e']
print(piano_keys[2:5:2]) # ['c', 'e']
print(piano_keys[::2]) # ['a', 'c', 'e', 'g']
print(piano_keys[::-1]) # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# tuple is available
piano_tuple = ["do", "re", "mi", "fa", "so", "la", "ti"]
print(piano_tuple[2:5]) # ['mi', 'fa', 'so']
