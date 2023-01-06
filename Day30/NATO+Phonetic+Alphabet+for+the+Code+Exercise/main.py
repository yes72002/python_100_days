import pandas


data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# keep_going = True
# while keep_going:
#     try:
#         word = input("Enter a word: ").upper()
#         output_list = [phonetic_dict[letter] for letter in word]
#         keep_going = False
#     except KeyError:
#         print("Sorry, only letters in the alphabet please.")
#         # word = input("Enter a word: ").upper()
#         keep_going = True
#     else:
#         print(output_list)

def generate():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate()
    else:
        print(output_list)

generate()

print("123")