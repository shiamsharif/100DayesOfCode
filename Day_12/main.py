""" scope """
# shiam = 32

# def frnd():
#     shiam = 106
#     print(shiam)


# frnd()
# print(shiam)



"""global scope"""
# shiam = 32

# def uni():
#     def frnd():
#         shawon = 106
#         print(shiam)  
#     frnd()

# uni()

"""This is no block space"""
# print("This is no block space")
# game_level = 3

# def bug():
#     bugs = ["bug1", "Bug2", "bug3"]
#     if game_level < 5:
#         new_bug = bugs[0]

#     print(new_bug)

# bug()

"""Modifying global scope DON'T DO THIS """
# shiam = 32

# def frnd():
#     global shiam
#     print(f"vitor : {shiam}")
#     shiam +=  100
#     print(shiam)

# frnd()

# print(f"byre ami : {shiam}")

# shiam = 32


"""Modifying global scope  """
# shiam = 32

# def frnd():
    
#     print(f"vitor : {shiam}")
#     return shiam+100

# shiam = frnd()

# print(f"byre ami : {shiam}")

"""global Constant"""

PI =3.14159

def c():
    print(PI)


c()