# 엔지니어 클래스
class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print("{}(으)로 프로그래밍합니다.".format(self.favorite_language))

# 테니스 선수 클래스
class TennisPlyer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다.".format(self.tennis_level))


class EngineerTennisPlayer(Engineer, TennisPlyer):
    def __init__(self, favorite_language, tennis_level):
        Engineer.__init__(self, favorite_language)
        TennisPlyer.__init__(self, tennis_level)

# 다중 상속을 받는 클래스의 인스턴스 생성
younghoon = EngineerTennisPlayer("파이썬", "초급")

# 두 부모 클래스의 메소드들을 잘 물려받았는지 확인
younghoon.program()
younghoon.play_tennis()

print(EngineerTennisPlayer.mro())
# __init__의 파라미터의 순서에 따라 상속 순서가 달라진다.

# 자바는 다중 상속 지원 하지 않는다. 오직 하나의 부모 클래스만을 받는다.
# 다중 상속의 위험성을 피하기 위해 부모 클래스 A, 부모 클래스 B, 자식 클래스 중
# 자식 클래스를 오버라이딩하는 방법이 있긴하다.

# 부모 클래스끼리 같은 이름의 메소드를를 갖지 않도록 하기
# 같은 이름의 메소드는 자식클래스에서 오버라이딩
