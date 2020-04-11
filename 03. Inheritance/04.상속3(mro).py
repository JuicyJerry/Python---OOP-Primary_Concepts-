# mro: Method Resolution Order: 메소드 검색 순서
# 메소드 검색 방향: 자식 -> 부모 => 오버라이딩 가능
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

print(Cashier.mro())

young = Cashier("강영훈", 8000, 4)
young.raise_pay()
