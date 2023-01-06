# try: # Something that might cause an exception
# except: # Do this if there was an exception
# else: # Do this if there was no exception
# finally: # Do this no matter what happens

# do not use bare 'except'
# because bare 'except' is going to ignore all errors.
# FileNotFound
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["asdfgh"])
# except: # from third line to this line
#     # print("There was an error")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# in try:, it will constantly execute to the last line,
# and ignore all previous errors above

# FileNotFound
try:
    file = open("a_file.txt")
    # print("1")
    a_dictionary = {"key":"value"}
    # print(a_dictionary["asdfgh"])
    print(a_dictionary["key"])
except FileNotFoundError: # from first line to this line if a_file.txt doesn't exist
    # print("2")
    # print("There was an error")
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_megssage:
    print(f"That key {error_megssage} does not exist.")
else: # no exception
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    raise TypeError("This is an erroe that I made up.")


# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)
