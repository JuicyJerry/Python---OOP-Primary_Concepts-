# 상속이란?
# 두 클래스 사이에 부모-자식 관계를 설정하는 것
# class #1: Benz class / class #2: car class
# 벤츠는 자동차다 (O), / 자동차는 벤츠다 (X)
# A는 B이다. #2가 부모 class, #1가 자식 classd이며 #2의 변수(색깔, 크기), 메소드(달린다, 멈춘다)를 #1가 물려받는다.

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
        #인스턴스 메소드
        return Cashier.company_name + " 계산대 직원: " + self.name

class Cashier(Employee):
    pass

younghoon = Cashier("강영훈", 8000)
younghoon.raise_pay()
print(younghoon.wage)
print(younghoon)

#help(Cashier)
# class의 정보를 자세히 출력하는 help함수
# builtins.object, 모든 class는 builtins.object의 자식 클래스


## 상속과 관련된 메소드와 함수
class DeliveryMan(Employee):
    pass
janghoon = DeliveryMan("이장훈", 10000)
janghoon.raise_pay()
print(janghoon.wage)
print(janghoon)

print(DeliveryMan.mro())
# 이렇게 하면 Cashier 클래스가 상속하는 부모 클래스를 볼 수 있습니다. 이 경우에 object 클래스는
# Cashier 클래스의 입장에서 부모 클래스의 부모 클래스입니다.

print(list.mro())

print(IndentationError.mro())
# IndentationError 클래스의 집안 내력(?)을 순서대로 한 번에 파악할 수 있다.


hodong = Cashier("호동", 5000)
# isinstance 함수는 어떤 인스턴스가 주어진 클래스의 인스턴스인지 알려줍니다.
# 첫 번째 파라미터에는 검사할 인스턴스의 이름
# 두 번째 파라미터에는 기준 클래스의 이름

print(isinstance(hodong, Cashier))
print(isinstance(hodong, DeliveryMan))
print(isinstance(hodong, Employee))
# 여기서 중요한 것은 마지막 줄에서 isinstance(young, Employee) 가 True 를 리턴한다는 사실입니다.
# Cashier 클래스는 Employee 클래스를 상속받는 자식 클래스입니다.
# 이 점이 아주아주 중요한데요.
# 즉, 상속 관계에 있는 두 클래스가 있을 때, 자식 클래스로 만든 인스턴스는 부모 클래스의 인스턴스이기도 하다는 점을 뜻합니다.
# 이 점은 나중에 ‘다형성’이라는 것을 설명할 때 핵심이 되는 원리입니다. 잊지 말고 꼭 기억해주세요!

class Manager(Employee):
    pass

# 첫 번째 파라미터에는 검사할 인스턴스의 이름
# 두 번째 파라미터에는 기준 클래스의 이름
print(issubclass(Cashier, Employee))
print(issubclass(Cashier, object))
print(issubclass(Manager, Employee))
print(issubclass(Employee, list)) # list 클래스와 아무런 관련이 없으므로 False

