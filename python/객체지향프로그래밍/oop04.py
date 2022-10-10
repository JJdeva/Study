class Dog:
    def __init__(self, name):
        self.name = name
    # str magic method
    def __str__(self):
        return self.name

    def __getattribute__(self, name):
        print(f"they want to get {name}")
        return "Hello"

jia = Dog('jia')
print(jia)