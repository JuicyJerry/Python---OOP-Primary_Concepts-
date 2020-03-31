# 술집 출입문 프로그램을 만든다고 가정했을 때
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

# 술집 출입문 프로그램
young = Citizen("강영훈", 25, "12345678")

# 음주 가능 나이인지 확인
if young.age >= Citizen.drinking_age:
    print("{}님은 음주 가능 나이입니다!".format(young.age))

# 음주 가능 나이인지 확인
if young.age >= Citizen.drinking_age:
    print("들어오세요~!")

# 음주 가능 나이인지 확인
if young.age >= Citizen.drinking_age:
    print("무슨 술을 드시겠습니까까")


# 만약 출생기준 나이 세는 기준이 0 -> 1 로 변한다면 밑에 코드 보다는
young = Citizen("강영훈", 25, "12345678")

# 음주 가능 나이인지 확인
if young.age + 1 >= Citizen.drinking_age:
    print("{}님은 음주 가능 나이입니다!".format(young.age))

# 음주 가능 나이인지 확인
if young.age + 1 >= Citizen.drinking_age:
    print("들어오세요~!")

# 음주 가능 나이인지 확인
if young.age + 1 >= Citizen.drinking_age:
    print("무슨 술을 드시겠습니까까")


# 이렇게, 이미 원하는 기능이 있는 메소드를 활용해서 이용하는 것이 더 유지봇수에 좋다.
young = Citizen("강영훈", 25, "12345678")

# 음주 가능 나이인지 확인
if young.age.can_drink():
    print("{}님은 음주 가능 나이입니다!".format(young.age))

# 음주 가능 나이인지 확인
if young.age.can_drink():
    print("들어오세요~!")

# 음주 가능 나이인지 확인
if young.age.can_drink():
    print("무슨 술을 드시겠습니까까")

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self.age +1 >= Citizen.drinking_age

# 직접 변수 사용 촤소화 => 유지보수 쉬운 코드

