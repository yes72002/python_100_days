# with open("weather_data.csv") as file:
#     data = file.readlines() # list
#     print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     # print(data) # object
#     temperatures = []
#     for row in data:
#         print(row) # list
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

# Pandas library and this is a python data analysis library
# which is super helpful and super powerful to perform data analysis on tabula.
import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
print(type(data)) # pandas,DataFrame
# print(data["temp"])
print(type(data["temp"])) # pandas,Series

data_dict = data.to_dict()
print(data_dict)

temp_dict = data["temp"].to_list()
print(temp_dict)
# challenge: average temperatures
average = sum(temp_dict) / len(temp_dict)
print(average)
print(data["temp"].mean()) # use series.method
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in row
print(data[data.day == "Monday"])

# challenge: print the row of data which had the highest temperature.
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

# challenge: convert monday's temperature from Celsius to Fahrenheit
monday_temp_F = (monday.temp)*1.8 + 32
print(monday_temp_F)

# Create a dat frame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
