# import csv
#
# # with open("weather_data.csv") as csv_file:
# #     weather_data = csv_file.readlines()
# #     print(weather_data)
#
# with open("weather_data.csv") as csvfile:
#     data = csv.reader(csvfile)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
#
# # print(data["condition"])
# print(data.condition)

# Get Data in Row

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# print(data[data.condition == "Sunny"])
# print(data[data.temp > 20])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# temp_c = monday.temp[0]
# print(temp_c)
# temp_f = temp_c * 9 / 5 + 32
# print(temp_f)

# # Create a dataframe
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [75, 55, 65],
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("scores.csv")

# Squirrel Count

# My_solution_1
# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# counts = squirrel_data.groupby("Primary Fur Color").size()
# print(type(counts))
# counts.to_csv("fur_counts_1.csv")

# My_solution_2
# fur_counts = squirrel_data["Primary Fur Color"].value_counts()
# print(fur_counts)
# fur_counts.to_csv("fur_counts.csv")

# The Solution
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")