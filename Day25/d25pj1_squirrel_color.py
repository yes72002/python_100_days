import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# my method
# color_list = data["Primary Fur Color"].to_list()
# gray_num = 0
# cinnamon_num = 0
# black_num = 0
# # print(color_list)
# for color in color_list:
#     if color == "Gray":
#         gray_num += 1
#     elif color == "Cinnamon":
#         cinnamon_num += 1
#     elif color == "Black":
#         black_num += 1

# angela's method
gray_num = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_num = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_num = len(data[data["Primary Fur Color"] == "Black"])

print(gray_num)
print(cinnamon_num)
print(black_num)

squirrel_data = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [gray_num, cinnamon_num, black_num],
}
squirrel_count = pandas.DataFrame(squirrel_data)
squirrel_count.to_csv("squirrel_count.csv")