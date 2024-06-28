""" *args """
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum 

# print(add(1,2,5,4,8,9,6,4,10,54,312,26,414,7,20,6))


""" **kwargs """
# def calculate(num, **kwargs):
#      #print(kwargs)
#     num += kwargs["add"]    # 2+3=5
#     num *= kwargs["multiply"]   # 5*5=25
#     print(num) # 25


# calculate(2, add = 3, multiply = 5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
    
    def print(self):
        print(f"The car is {self.model} made by {self.make}")

my_car = Car(make="BMW")
my_car.print()