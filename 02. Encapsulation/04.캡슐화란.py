class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

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

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self.__age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0:
            print("나이는 0보다 적을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다")
            self.__age = 0
        else:
            self.__age = value


# 시민 인스턴스 생성
young = Citizen("younghoon kang", 15, "87654321") # (1)
print(dir(young))                                 # (2)

# (1) Citizen 클래스로 young이라는 인스턴스를 하나 생성할게요.
# (2) dir 라는 함수를 사용하면 인스턴스가 갖고 있는 모든 변수와 메소드를 볼 수 있는데요.

# 사실 변수나 메소드 이름 앞에 밑줄 두 개(__)를 쓰면, 파이썬은 그 앞에 추가적으로 "_클래스 이름" 을 덧붙여서 이름을
# 바꿔버립니다. 이걸 파이썬에서는 네임 맹글링(name mangling)이라고 합니다. 맹글링(mangling)의 동사형인 맹글(mangle)은
# 영어로 "마구 썰다", "엉망진창으로 만들다"라는 뜻입니다. 여기서는 이름을 새로운 형태로 변환하는 것을 맹글링이라고 하는 겁니다.

# 그럼 이 바뀐 이름으로는 클래스 밖에서도 접근할 수 있지 않을까요? 아래 코드는 바뀐 이름으로 변수에 접근하는 코드입니다.
# 시민 인스턴스 생성
young = Citizen("younghoon kang", 15, "87654321")

print(young._Citizen__age) # 출력: 15
print(young._Citizen__resident_id) # 출력: 87654321

young._Citizen__age = -10
print(young) # 출력: younghoon kang씨는 -10살입니다!

# 사실 파이썬은 언어 차원에서 캡슐화를 지원하지 않습니다. 캡슐화처럼 보이긴 하지만 알고보면 완벽한 캡슐화는 아닙니다.
# 다른 객체 지향 언어인 Java에서는 private이라는 키워드를 변수 이름 앞에 붙이면, 외부로부터의 접근이 완벽히 차단됩니다.
# 파이썬처럼 바뀐 새 이름으로 접근할 수 있다거나 하는 방법도 없습니다. Java에서는 캡슐화가 완벽하게 되는 것이죠.
# 하지만 파이썬이 캡슐화를 지원하지 않는다고 해서 캡슐화를 아예 무시하는 것은 아닙니다. 파이썬 세계의 개발자들은 조금
# 다른 방식으로 캡슐화를 하는데요. 다음 영상에서 설명할게요.

# 파이썬 문화(언더바 하나) - 접근하지 말라는 경고 표시
# '_변수 _메소드', 'getter / setter' or '다른 용도의 메소드 추가' 를 해준다.
