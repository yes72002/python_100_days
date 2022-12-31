# read file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# ''' 
# lots of code
# '''
# file.close()

# Now we no longer have to remember to close our file just by add some keywords here.
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# write file 
# with open("my_file.txt") as file:
    # file.write("New text.") # io.UnsupportedOperation: not writable
                              # because we open up the file in read-only mode

# write mode
# with open("my_file.txt", mode="w") as file: # delete everything
    # file.write("New text.")

# append mode
with open("my_file.txt", mode="a") as file: # append
    file.write("\nNew text.")

# if you try to open a file in write mode and that file doesn't exist, 
# then it's going to actually create it for you from scratch.
with open("new_file.txt", mode="a") as file:
    file.write("New text.")

# Absolute File Path
# C:/Users/Jim/Desktop
# Relative  File Path
# ./<file> = <file>
# forward slash: /
# backward slash: \
# in a Mac, each of the folders are sepatated by a forward slash /
# whereas on Windows, they're separated by a \
# Python doesn't care
