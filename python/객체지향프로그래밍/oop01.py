# constructore 메소드 -> class가 생성될 때 호출되는 함수
class Player:

    def __init__(self, name, xp):
        self.name = name
        self.xp = xp

    def say_hello(self):
        print("hello!")

if __name__ == "__main__":
    nico = Player("nico", 1000)
    print(nico.name, nico.xp)
    print(nico.say_hello())