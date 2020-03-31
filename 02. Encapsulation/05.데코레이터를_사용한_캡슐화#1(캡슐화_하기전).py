# Q. 왜 파이썬은 언어 자체에서 캡슐화를 지원하지 않을까요?
# A. 파이썬의 문화 때문입니다. -> 캡슐화를 안 해도 OK! 해도 OK!
# 나중에 캡슐화를 하고 싶을 때는?

# 캡슐화 전
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


young = Citizen("younghoon kang", 15, "87654321")
print(young.age)    # 출력: 15
young.age = 30
print(young.age)    # 출력: 30
