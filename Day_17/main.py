class User:
    def __init__(self,id,name):
        self.id = id
        self.name = name
        self.emni = "emni"

    def Print(self):
        print(f"My name is {self.name} and id {self.id}")


user_1 = User("41220100032", "shiam")
user_1.Print()

print(user_1.emni)


# print(user_1.username)



# user_2 = User()
# user_2.id = "41220100032"
# user_2.username = "Shiam"

# print(user_2.username)