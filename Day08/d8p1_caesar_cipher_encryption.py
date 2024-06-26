alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# use list to complete
def encrypt_list(text, shift):
    text_list = list(text)
    encrypt_text = []
    for letter in text_list:
        position = alphabet.index(letter)
        new_position = position + shift
        encrypt_text.append(alphabet[new_position])
        # for i in range(0, len(alphabet)):
        #   if letter == alphabet[i]:
        #     print(i)
        #     encrypt_text += int(i) # TypeError: 'int' object is not iterable
    encrypt_text_str = ''.join(encrypt_text)
    print(f"The encoded text is {encrypt_text_str}")

# angela
# use string to complete
def encrypt_string(text, shift):
    encrypt_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        encrypt_text += alphabet[new_position]
    print(f"The encoded text is {encrypt_text}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt_list(text = "hello", shift = 2)
encrypt_string(text = "hello", shift = 2)