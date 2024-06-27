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


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number**2 for number in numbers]
print(squared_numbers)