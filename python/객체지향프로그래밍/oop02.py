# super -> 상속
# 상속을 통해 중복되는 부분을 추상화시켜보자.
class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello! My name is {self.name}")

# super() -> 상속받는 부모클래스를 호출해주는 메소드
class Player(Human):
    def __init__(self, name, xp):
        # 부모클래스를 호출하면서 init메소드 호출하고, name인자 전달
        super().__init__(name)
        self.xp = xp


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team



if __name__ == "__main__":
    nico = Player("nico", 1000)
    nico.say_hello()
    nico_fan = Fan("nico_fan", "dontknow")
    nico_fan.say_hello()