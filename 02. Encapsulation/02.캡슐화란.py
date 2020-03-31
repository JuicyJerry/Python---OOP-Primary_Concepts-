# 캡슐화의 정의
# 1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것
# 2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것


# 2
# 접근할 수 있는 메소드를 만드는 것 : 캡슐화의 2번째 정의
# citizen 클래스: can_drink 메소드, get_age 메소드, set_age 메소드를 통해서만 사용 가능하는데
# __age 변수 접근하는 통로를 메소드로 제한하는 것을 속성과 행동을 하나로 묶는다는 의미
class Citizen:
    """주민 클래스"""
    drinking_age = 19   # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.__age = age
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

    def set_age(self, value):   # setter method: 변수의 값을 설정하는 메소드
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        self.__age = value

young = Citizen("younghoon", 18, "12345678")

print(young.get_age())

# 왜 __resident_id 는 getter, setter 메소드를 안 만드나요? => 민감한 정보 => 값을 읽거나 설정하며 안 된다.
# #51는 id를 읽거나 설정하는 메소드가 아니라 id가 맞는지 확인 하는 메소드이다. 꼭 getter / setter 메소드를 만들 필요는 없다.

# 캡술화 정리
# (1) 클래스 밖에서 접근 못하게 할 변수, 메소드 정하기
# (2) 변수나 메소드 이름 앞에 언더바 2개 붙이기
# (3) 변수에 간접 접근할 수 있게 메소드 추가하기 -> getter / setter or 다른 용도의 메소드
