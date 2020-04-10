# 신용 카드를 나타내는 CreditCard 클래스를 만들고 싶습니다. CreditCard 클래스에는 소유자 이름, 비밀 번호, 카드 한도 정보
# 가 저장됩니다. 다음 조건들에 맞게 CreditCard 클래스를 완성하세요.
# CreditCard 클래스의 모든 인스턴스 변수들에 밑줄 두 개를 써서 외부에서 직접 접근하지 못하게 해주세요. (__name, __password, __payment_limit)
# 각 인스턴스 변수는 getter/setter 메소드를 갖습니다. 각 getter/setter 메소드의 이름 형식은 get_변수이름, set_변수이름으로 합니다.


class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_password(self):
        return "비밀 번호는 볼 수 없습니다"

    def set_password(self, value):
        self.password = value

    def get_payment_limit(self):
        return self.__payment_limit

    def set_payment_limit(self, value):
        #self.__payment_limit = value

        if 0 <= value <= CreditCard.MAX_PAYMENT_LIMIT:
            # 0과 max 사이는 0, max를 포함한다는 뜻
            self.__payment_limit = value
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")





card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())
