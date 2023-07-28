# num_char = len(input("What is your name? "))
# print("your name has " +num_char+" charracters.")

# TypeError: can only concatenate str (not "int") to str


num_char = len(input("What is your name? "))

new_num_char =str(num_char)

print("your name has " +new_num_char+" characters.")


a=1254
print(type(a)) #<class 'int'>

a=str(1235)
print(type(a)) #<class 'str'>

print(70 + float("100.5")) #170.5
print(int(10.21))