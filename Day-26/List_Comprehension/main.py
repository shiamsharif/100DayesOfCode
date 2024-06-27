# num = [1,2,3]
# new_list = [n+1 for n in num]
# print(new_list)


# name = "shiam"
# new_list = [n for n in name]
# print(new_list)


# list = [n*2 for n in range(1,5)]
# print(list)


""" Conditional List Comprehension """
# names = ["Sam", "Alex", "Jo", "shiam", "shaman", "Savrin","Fa", "Zarifah"]
# short_name = [name.upper() for name in names if not len(name) < 5]
# print(short_name) 


""" Exercise-1 """
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [number**2 for number in numbers]
# print(squared_numbers)


""" Exercise-2 """
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [number for number in numbers if number % 2 == 0]
# print(result)


""" Exercise-3 """
""" Solution: 1 """
# import pandas as pd

# # Read the text files into DataFrames
# datafile1 = pd.read_csv("file1.txt", header=None, names=['value'])
# datafile2 = pd.read_csv("file2.txt", header=None, names=['value'])

# # Convert the 'value' column to a set of integers
# set1 = set(datafile1['value'])
# set2 = set(datafile2['value'])

# # Find the intersection of both sets
# common_values = set1.intersection(set2)

# print("Common integers in both files:", common_values)


""" Solution: 2 """
with open("./file1.txt") as file1:
    file_1_Data = file1.readlines()
with open("./file2.txt") as file2:
    file_2_Data = file2.readlines()
    
result = [int(num) for num in file_1_Data if num in file_2_Data]
print(result)