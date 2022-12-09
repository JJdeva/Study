class User:
    count = 0 # 클래스 변수 선언
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
        User.count += 1 # User인스턴스 생성될 때마다 1씩 증가

    def __str__(self):
        return self.name
    
user1 = User('user1', '12345') 
print(User.count)
user2 = User('user2', '54321')
print(User.count)
user3 = User('user3', '67890')
print(User.count)