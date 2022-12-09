# 상속

# 부모클래스
class Employee:
    """직원 클래스"""
    company_name = "맥도리아" # 가게 이름
    raise_percentage = 1.03 # 시급 인상률

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name # 이름
        self.wage = wage # 시급

    def raise_pay(self):
        """시급을 인상하는 메소드"""
        self.wage = self.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


# 자식클래스 1
class Cashier(Employee):

    # 변수 오버라이딩
    raise_percentage = 1.05

    # 메소드 오버라이딩
    def __init__(self, name, wage, number_sold):
        # Employee.__init__(self, name, wage) # 부모 클래스의 init메소드를 활용
        super().__init__(name, wage)
        # 이때 self를 쓸 필요가 없다.
        self.number_sold = number_sold

    def __str__(self):
        return Employee.company_name + " 계산대 직원: " + self.name


# 자식클래스 2
class DeliveryMan(Employee):
    pass

print(Cashier.mro())