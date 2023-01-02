sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
# google: how to convert a sentence into a list of words.
# string.split()
sentence_list = sentence.split()
result = {words:len(words) for words in sentence_list}
print(result)