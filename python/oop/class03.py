class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

user = User('김길동', '1234')
print(user)

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __str__(self):
        return self.name


user = User('길동이', '1234')
print(user)