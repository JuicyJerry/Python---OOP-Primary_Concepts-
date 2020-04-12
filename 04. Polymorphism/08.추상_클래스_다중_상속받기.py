"""이전에 다중 상속이 무엇인지 배웠습니다. 다중 상속은 되도록 하지 않거나 하더라도 주의해서 해야한다고 말씀드렸죠?
하지만 이러한 주의사항은 추상 클래스가 아닌 일반 클래스에 해당되는 내용입니다.
추상 클래스 여러 개를 다중 상속받는 것은 일반적으로 많이 쓰입니다. 아래의 코드를 볼까요?"""
# 1. 추상 클래스 다중 상속 예시
from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:
        pass

class Email(Message, Sendable):
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email

    def print_message(self):
        print("이메일 내용입니다:\n{}".format(self.content))

    def send(self, destination):
        print("이메일을 주소 {}에서 {}로 보냅니다!".format(self.user_email, destination))
"""추상 클래스 Message와 Sendable을 다중 상속받는 Email 클래스를 정의했습니다. 그리고 각 추상 클래스의 추상 메소드들인
 print_message와 send 메소드를 잘 오버라이딩했군요. 
 
 Email 클래스를 사용해보면,"""
# 이메일 인스턴스를 생성한다.
email = Email("안녕? 오랜만이야 잘 지내니?", "young@codeit.kr")

# 메시지 내용 출력
email.print_message()
# 메시지 전송
email.send("captain@codeit.kr")

# 실행 결과
"""이메일 내용입니다:
안녕? 오랜만이야 잘 지내니?
이메일을 주소 young@codeit.kr에서 captain@codeit.kr로 보냅니다!

잘 동작합니다!"""

# 2. 추상 클래스 다중 상속: 추상 메소드가 겹칠 때
"""그렇다면 왜 추상 클래스를 다중 상속받는 것은 일반 클래스 다중 상속보다 좀더 괜찮은 것일까요? 일단 아래 코드처럼 
Message 추상 클래스도 Sendable 추상 클래스의 추상 메소드와 같은 이름의 메소드로 send 메소드를 갖도록 합시다."""
class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

    @abstractmethod
    def send(self, destination: str) -> None:  # ----- 중복되는 추상 메소드
        pass

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None: # ----- 중복되는 추상 메소드
        pass
"""이렇게 두 추상 클래스 사이에 중복되는 메소드(send 메소드)가 있어도 방금 전 코드는 다음과 같이 잘 동작합니다."""
# 이메일 인스턴스를 생성한다.
email = Email("안녕? 오랜만이야 잘 지내니?", "young@codeit.kr")

# 메시지 내용 출력
email.print_message()
# 메시지 전송
email.send("captain@codeit.kr")

"""실행 결과
이메일 내용입니다:
안녕? 오랜만이야 잘 지내니?
이메일을 주소 young@codeit.kr에서 captain@codeit.kr로 보냅니다!"""

"""사실 생각해보면 딱히 결과가 바뀔 이유가 없습니다. 자식 클래스는 어차피 상속받는 추상 클래스들의 모든 추상 메소드를 
오버라이딩해야 합니다. 아무리 부모 추상 클래스들에 같은 이름의 추상 메소드들이 있다해도 어차피 자신이 오버라이딩한 
내용이 반영됩니다. 따라서 만약 부모 추상 클래스들 사이에 겹치는 메소드가 추상 메소드라면 문제없이 다중 상속을 할 수 
있습니다. 
하지만 일반 메소드가 겹친다면 문제가 발생합니다."""

# 3. 추상 클래스 내 일반 메소드
class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

    def __str__(self): # ----- 중복되는 일반 메소드
        return "Message 클래스의 인스턴스"

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:
        pass

    def __str__(self): # ----- 중복되는 일반 메소드
        return "Sendable 클래스의 인스턴스"

""""위 코드와 같이 부모 추상 클래스 간에 추상 메소드가 아닌 일반 메소드가 겹친다면 일반 클래스를 다중 상속할 때와 
마찬가지로 주의해야합니다. 자식 클래스에서 일반 메소드를 오버라이딩하지 않으면 어느 추상 클래스의 일반 메소드를 
실행해야하는지 애매모호하기 때문입니다. 물론 이전에 배운대로 파이썬에서는 mro라는 나름의 규칙이 있었지만요."""


# 정리
"""기억할 것

정리하자면 이 세 가지를 기억하셔야 합니다:

1. 추상 클래스 다중 상속은 일반적으로 많이 사용한다.
2. 다중 상속받는 부모 추상 클래스들이 추상 메소드로만 이뤄져 있으면 아무 문제 없이 다중 상속받을 수 있다.
3. 다중 상속받는 부모 추상 클래스들 간에 이름이 겹치는 일반 메소드가 있으면 일반 클래스를 다중 상속받을 때와 동일한 
문제가 생길 수 있다."""
