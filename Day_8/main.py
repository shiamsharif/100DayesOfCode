# def greet():
#     print("print 1")
#     print("print 2")
#     print("print 3")

# greet()

#TODO:function allows for input
# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}")

# greet_name("Shiam")  

#TODO:Function with more than one input
# def greet_with(name,location):
#     print(f"Hello, This is {name}.")
#     print(f"I live in {location}.")

# greet_with("Shiam","Jashore")

#TODO: Function with key word argument
def greet_with(name="Shiam",location="Jashore"):
    print(f"Hello, This is {name}.")
    print(f"I live in {location}.")

greet_with("Sharif","Dhaka")