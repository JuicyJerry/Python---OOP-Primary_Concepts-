# 추상화 잘하기
# 1. 이름을 잘 짓기
# 어디에 쓰는 클래스이고 어떻게 사용할지 직관적으로 알 수 있어야 한다.

# 2. 문서화(docstring) 하기 # documentation string
# A 클래스는 ~~~를 위해 만들어졌습니다. 이렇게 저렇게 사용하세요.
# B 변수는 인스턴수 변수로 실수형입니다.
# C 메소드는 잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드

class BankAccount:
    """은행 계좌 클래스"""

    def __init__(self, owner_name, balance):
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드드"""
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def add_interest(self):
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance += 1 + BankAccount.interest()

# 클래스를 어떻게 사용할 수 있을지 직관적으로 알 수 있다!

# 3. help(Class)
help(BankAccount)
#help(list)
# 사용할 수 있는 메소드의 리스트

# 4. 문서화 스타일 3가지

#def find_suggestion_videos(self, number_of_suggestions=5):

# Google docstring:
"""유저에게 추천할 영상을 찾아준다
Parameters:
  number_of_suggestions (int): 추천하고 싶은 영상 수
    (기본값은 5)

Returns:
  list: 추천할 영상 주소가 담긴 리스트
"""

# reStructuredText (파이썬 공식 문서화 기준):
"""유저에게 추천할 영상을 찾아준다
    
:param number_of_suggestions: 추천하고 싶은 영상 수
  (기본값은 5)
:type number_of_suggestions: int
:returns: 추천할 영상 주소가 담긴 리스트
:rtype: list
"""

# NumPy/SciPy (통계, 과학 분야에서 쓰이는 Python 라이브러리):
"""유저에게 추천할 영상을 찾아준다
    
Parameters
----------
number_of_suggestions: int
  추천하고 싶은 영상 수 (기본값은 5)
    
Returns
-------
list 
  추천할 영상 주소가 담긴 리스트
"""


# 문서화에서 가장 중요한 것은 프로그램을 함께 만드는 팀원들과 이러한 문서화 포맷에 관해 미리 약속을 하고 이를 잘 지키는 것입니다.
# 변수, 함수, 클래스 모두 추상화의 예시들이다.
# 1. 변수는 이름만 알면 어떤 값이 저장되어 있는지 알 필요가 없다.
# 2. 함수는 그 구현 내용을 알지 못해도 파라미터만 잘 넣어주고 호출하면 사용할 수 있습니다.
# 3. 클래스는 어떤 변수와 메소드가 정의되어 있는지만 알면 각각의 세부 구현 내용을 몰라도 사용할 수 있습니다.
# 
# 클래스 내부의 속성을 외부로 숨길 수 있다. (X)
# - '클래스 내부의 속성을 외부로부터 숨길 수 있다'는 설명은 '캡슐화'에 대한 설명이다.
