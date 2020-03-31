# 캡슐화 후
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self._resident_id = resident_id

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self._resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self.age) + "살입니다!"

    def get_age(self):
        """술겨 놓은 인스턴스 변수 _age의 값을 받아오는 메소드"""
        return self.get_age()
    def set_age(self, value):
        """술겨 놓은 인스턴스 변수 _age의 값을 받아오는 메소드"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다.")
            self._age = 0
        else:
            self._age = value

young = Citizen("younghoon kang", 15, "87654321")
print(young.get_age())    # 출력: 15
young.set_age(30)
print(young.get_age())    # 출력: 30
