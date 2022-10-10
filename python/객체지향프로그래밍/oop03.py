class Dog:
    def woof(self):
        print("woof woof")

# 이럴땐 super가 없어도 에러발생X. 부모클래스가 초기화해주는 부분이 없기때문에
# 근데 꼭 super가 초기화해줄때만 사용하는건 아님
class Beagle(Dog):
    def jump(self):
        # 부모호출과 동시에 메소드 실행 -> print("woof woof")
        super().woof()
        print('Jump')

if __name__ == "__main__":
    dog = Beagle()
    dog.jump()