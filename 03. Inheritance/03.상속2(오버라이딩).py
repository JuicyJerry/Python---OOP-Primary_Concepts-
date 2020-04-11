# 자식 클래스들은 부모클래스의 공통부분만 물려받게 될 경우 자식 클래스 간의
# 차이가 없어 두 클래스를 제대로 사용할 수 없다.
# => 각 클래스에 맞게 수정: 오버라이딩

class Employee:
    """직원클래스"""
    company_name = "코드잇 버거"     # 가게 이름
    raise_percentage = 1.03          # 시급 인상률

    def __init__(self, name, wage, number_sold = 0):
        self.name = name        # 이름
        self.wage = wage        # 시급

    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def __str__(self):
        # dunder str
        return Cashier.company_name + " 직원: " + self.name

# 오버라이딩 => 자식 클래스에서 물려받은 메소드 => 같은 이름의 메소드를 내용을 바꿔 정의
class Cashier(Employee):
    raise_percentage = 1.05          # 시급 인상률

    def __init__(self, name, wage, number_sold):
        Employee.__init__(self, name, wage)
        super().__init__(name, wage)
        # super 함수는 self 사용 안해도 되며, 부모 클래스의 메소드를 호출 가능

        self.number_sold = number_sold

    def __str__(self):
        return Cashier.company_name + "계산대 직원: " + self.name

class DeliverMan(Employee):
    pass

young = Cashier("강영훈", 8000, 4)
young.raise_pay()

print(Cashier.raise_percentage)
print(Cashier.company_name)

print(young.name)
print(young.wage)
print(young.number_sold)

print(young)
print(young.raise_percentage)
