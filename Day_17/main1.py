class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.followers = 0
        self.following = 0


    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(41220100032, "shiam")
user_2 = User(41220100042, "Mahadi")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)