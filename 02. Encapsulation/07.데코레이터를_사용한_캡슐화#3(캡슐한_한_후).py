# 캡슐화 후(중요한 개념!)
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.age) + "살입니다!"

    # 어떠한 변수에 대한 getter 메소드 역할로 설정
    """_age의 getter method 역할"""
    @property
    def age(self):
        print("나이를 리턴합니다.")
        return self._age

    """_age의 setter method 역할"""
    @age.setter
    def age(self, value):
        print("나이를 설정합니다.")
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value


young = Citizen("younghoon kang", 15, "87654321")
print(young.age)    # 출력: 15
young.age = 30
print(young.age)    # 출력: 30

# 데코레이터를 사용하면 #43, 45의 'young.age'가 실행될 때 getter method 자동 실행되어서 구문의 의미가 변함
# #44가 실행될 때 setter method가 자동 실행된다. 본래 'young.age'에 '30'를 대입하는 구문이지만
# 데코레이터가 붙어서 setter method가 실행하라는 뜻으로 변함
# 그 후 #34의 value의 #44의 30이 들어간다.

# property 데코레이터: 변수의 값을 읽거나 설정하는 구문 -> 아예 다른 의미로 실행
# Q. Citizen 클래스에는 age와 _age 중 어떤 인스턴스 변수가 있는 건가요?
# A. _age 입니다. age는 _age에 대한 getter 메소드, setter 메소드의 이름입니다.

# property 데코레이터 : 캡슐화 전 사용하던 코드를 캡슐화 적용 후 수정하지 않아도 된다.
# #43, 45이 실행될 때, #27의 age가 실행되고
# #44가 실행될 때, #32 setter 메소드가 실행된다. 사실 _age가 있는것이지만..

# 만약 getter / setter 메소드 적용하려고 하면
# young = Citizen("younghoon kang", 15, "87654321")
# print(young.get_age())    # 출력: 15
# young.set_age(30)
# print(young.get_age())    # 출력: 30
# 와 같이 작업해야 한다.



