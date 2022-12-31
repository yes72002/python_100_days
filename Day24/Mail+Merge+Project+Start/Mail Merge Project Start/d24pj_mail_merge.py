#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open("./Input/letters/starting_letter.txt") as file:
with open("Input/letters/starting_letter.txt") as starting_letter:
    contents = starting_letter.read() 
    # print(type(contents))
    # print(contents)

# my method 
# with open("Input/Names/invited_names.txt") as file:
#     names = file.read() # string
#     print(names)
#     name_list = names.split("\n") # list
#     print(name_list)

# Angela's method
# readlines(): Return all lines in the file, as a list where each line is an item in the list object.
with open("Input/Names/invited_names.txt") as invited_names:
    name_list = invited_names.readlines() # list
    # print(name_list)
    
for name in name_list:
    # strip(): Remove spaces at the beginning and at the end of the string. the same as \n
    name = name.strip()
    contents_new = contents.replace("[name]", name) # string
    # print(contents_new)
    with open(f"Output/ReadyToSend/invited_{name}.txt", mode="w") as file:
        file.write(contents_new)
