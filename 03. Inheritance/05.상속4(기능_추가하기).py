# 기능 추가하기
class Employee:
    """직원클래스"""
    company_name = "코드잇 버거"     # 가게 이름
    raise_percentage = 1.03          # 시급 인상률

    def __init__(self, name, wage):
        self.name = name        # 이름
        self.wage = wage        # 시급

    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def __str__(self):
        # dunder str
        return Cashier.company_name + " 직원: " + self.name

class Cashier(Employee):
    raise_percentage = 1.05          # 시급 인상률
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        Employee.__init__(self, name, wage)
        super().__init__(name, wage)
        # super 함수는 self 사용 안해도 되며, 부모 클래스의 메소드를 호출 가능

        self.number_sold = number_sold

    def take_order(self, money_received):
        """주문과 돈을 받고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다.")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + "계산대 직원: " + self.name

young = Cashier("강영훈", 8000, 0)
young.raise_pay()
print(young.wage)

print(young.take_order(7000))
print(young.take_order(3000))

print(young.burger_price)
print(Cashier.burger_price)

print(young.number_sold)
print(young)
