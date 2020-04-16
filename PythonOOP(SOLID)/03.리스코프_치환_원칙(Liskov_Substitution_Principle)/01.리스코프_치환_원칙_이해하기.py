"""리스코프 치원원칙
부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 대신 사용했을 때 코드가 원래 의도대로 작동해야 한다
자식 클래스의 인스턴스는 부모 클래스의 인스턴스이기도 하다. 즉, 부모 클래스의 행동규약을 자식 클래스가 위반하지 말 것

부모 클래스의 행동규약을 어긴다는 것은?
자식 클래스가 부모 클래스의 변수와 메소드를 상속 받기만 하면 문제가 없지만, 자식 클래스가 부모 클래스의 변수와 메소드를
오버라이딩 한다면, 잘못하면 리스코프 치환 원칙을 어길 수 있다.

자식 클래스가 오버라이딩을 잘못 하는 경우
1. 자식 클래스가 부모 클래스의 변수의 타입을 바꾸거나 메소드의 파라미터 또는 리턴값의 타입 or 갯수를 바꾸는 경우
2. 자식 클래스가 부모 클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우
"""

class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage #1 -> 숫자

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다"  #1-1 숫자 -> 문자 / 리스코프 치환원칙 위반


employee_1 = Employee("성태호", 7000)
employee_2 = Employee("강영훈", 6500)

cashier = Cashier("김대위", 9000)

employee_list = []
employee_list.append(employee_1)
employee_list.append(employee_2)
employee_list.append(cashier) #1 리스코프 치환원칙 위반

#for employee in employee_list:
#    employee.raise_pay()

total_wage = 0

for employee in employee_list:
    total_wage += employee.wage

print(total_wage)

"""
1. 부모 클래스 Employee(wage 리턴값 -> 숫자), wage 메소드는 숫자를 리턴한다
2. 자식 클래스 Cashier(wage 리턴값 -> 문자), wage 메소드는 숫자를 리턴한다
"""
