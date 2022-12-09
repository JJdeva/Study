# 유저클래스 정의
class User:
    pass


# 인스턴스 생성
# 같은 클래스라고 해도 서로 다 다른 인스턴스
user1 = User()
user2 = User()
user3 = User()

# 인스턴스 변수
user1.name = '김길동'
user1.email = 'rlfehd@naver.com'
user1.password = '12345'

print(user1)
print(user1.name)
print(user1.email)
print(user1.password)
print(dir(user1))