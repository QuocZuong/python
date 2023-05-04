# with open("/Users/quoczuong/Udemy/Python/Code/FinalProject/Day25/weather_data.csv") as data:
#     weather_data = data.readlines()
# list_of_day = []
# list_of_temp = []
# list_of_weather = []

# for each in weather_data:
#     temp = each.split(",")
#     list_of_day.append(temp[0])
#     list_of_temp.append(temp[1])
#     list_of_weather.append(temp[2])

# print(list_of_day)
# print(list_of_temp)
# print(list_of_weather)


# import csv
# with open("/Users/quoczuong/Udemy/Python/Code/FinalProject/Day25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     for each in temperatures:
#         print(each)


# tinh trung binh cong cua mot cot
# import pandas

# data = pandas.read_csv(
#     "/Users/quoczuong/Udemy/Python/Code/FinalProject/Day25/weather_data.csv")
# temperature_data = data["temp"].to_list()
# #ngoai data["temp"] thi co the su dung data.temp
# # count = 0
# # sum = 0
# # for each in temperature_data:
# #     sum += int(each)
# #     count += 1
# # print(sum/count)
# print(data["temp"].mean())
# result = sum(temperature_data)/len(temperature_data)
# print(result)


# import pandas

# data = pandas.read_csv(
#     "/Users/quoczuong/Udemy/Python/Code/FinalProject/Day25/weather_data.csv")

# # tim ngay co nhiet do cao nhat theo hang (row)
# # print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.temp)
# f_temperature = int(monday.temp) * 1.8 + 32
# print(f_temperature)

import pandas

data = pandas.read_csv(
    "/Users/quoczuong/Udemy/Python/Code/FinalProject/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

search_for = "Primary Fur Color"

gray_color = len(data[data[search_for] == "Gray"])
red_color = len(data[data[search_for] == "Cinnamon"])
black_color = len(data[data[search_for] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, red_color, black_color]
}

temp_file = pandas.DataFrame(data_dict)
temp_file.to_csv("/Users/quoczuong/Udemy/Python/Code/FinalProject/Day25/output.csv")
