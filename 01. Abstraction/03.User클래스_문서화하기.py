class User:
    """User 클래스: SNS의 유저를 나타내는 클래스"""
    count = 0

    def __init__(self, name, email, pw):
        """__init__ 메소드: 이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다"""
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        """say_hello 메소드: 유저의 이름을 포함한 인사 메시지를 출력한다"""
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        """__str__ 메소드: 유저 정보를 정의된 문자열 형태로 리턴한다"""
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        """number_of_users 메소드: 총 유저 수를 출력하는 클래스 메소드"""
        print("총 유저 수는: {}입니다".format(cls.count))

help(User)

# 1. 파이썬의 type hinting
# 파이썬은 동적 타입의 언어
i = 0
j = 0

#def add(x, y):
    # some code

# 자바는 정적 타입의 언어
#int i = 0;
#int j = 0;

#public int add(int x, int y) {
#    // some code
#}

# 동적 언어의 단점을 보완하고자 type hinting 기능을 추가하였다.
class BankAccount:
    """은행 계좌 클래스"""
    interest: float = 0.02

    def __init__(self, owner_name: str, balance: float) -> None:    # return 값
        """인스턴스 변수: name(문자열), balance(실수형)"""
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount만큼 늘려주는 메소드"""
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def withdraw(self, amount: float) -> None:
        """잔액 인스턴스 변수 balance를 파라미터 amount 만큼 줄인다"""
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount

    def add_interest(self) -> None:
        """잔액 인스턴스 변수 balance를 이자율만큼 늘려주는 메소드"""
        self.balance += 1 + BankAccount.interest
