# 캡슐화의 정의
# 1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것
# 2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것

class Citizen:
    """주민 클래스"""
    drinking_age = 19  # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self.__resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

    def get_age(self):  # getter method: 변수의 값을 읽는 메소드
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self.__age

    def set_age(self, value):  # setter method: 변수의 값을 설정하는 메소드
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        # self.__age = value # 나이가 음수 일 수 있다. setter method는 아래와 같이 점검하는 코드를 설정하는 것이 좋다.

        if value < 0:
            print("나이는 0보다 적을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self.__age = 0
        else:
            self.__age = value


young = Citizen("younghoon", -10, "12345678")
print(young.get_age())

young.set_age(-10)
print(young.get_age())

young.set_age(19)
print(young.get_age())


