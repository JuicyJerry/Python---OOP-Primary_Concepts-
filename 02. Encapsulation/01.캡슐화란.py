# 캡슐화의 정의
# 1. 객체의 일부 구현 내용에 대한 외부로부터의 직접적인 액세스를 차단하는 것
# 2. 객체의 속성과 그것을 사용하는 행동을 하나로 묶는 것

# 1
class Citizen:
    """주민 클래스"""
    drinking_age = 19   # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.age = age
        self.resident_id = resident_id

    def __authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.__age >= Citizen.drinking_age

    def __str__(self):
        """지민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.__age) + "살입니다!"

kyusik = Citizen("최규식", 25, "12345678")
kyusik.authenticate("12345678")

# __str__ 메소드는 이름 앞 뒤에 모두 밑줄 2개(__)가 있기 때문에 일반 메소드와 동일하게 사용할 수 있고,
# 인스턴스 변수 __resident_id는 앞에만 밑줄 2개(__)가 있어서 외부에서 접근할 수 없는 겁니다. __resident_id__로 바꿔주면
# 일반 변수처럼 사용할 수 있습니다.
# 앞으로 클래스에서 숨기고 싶은 변수나 메소드는 이름의 앞에만 밑줄 2개(__)를 붙여야겠죠?
