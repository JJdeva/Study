class User:
    # 인스턴스 매소드
    def say_hello(some_user):
        print(f'안녕하세요. {some_user.name}입니다.')


user1 = User()

user1.name = '김길동'

User.say_hello(user1)
user1.say_hello()