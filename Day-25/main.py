""" 1 """
# with open("./002 weather-data.csv") as weather_data:
#     data = weather_data.readlines()


""" 2 """
# import csv

# with open("./002 weather-data.csv") as data_File:
#     data = csv.reader(data_File)
#     temperatures = []
#     for row in data:
#         try:
#             temperatures.append(int(row[1]))
#         except ValueError:
#             pass
 
# print(temperatures)


""" 3 """
#step 1:  pip install pandas
import pandas 

data = pandas.read_csv("./002 weather-data.csv")
# print(data["temp"]) 

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())
print(data["temp"].max())

""" Get Date in columns """
print(data["condition"])
print(data.condition)
