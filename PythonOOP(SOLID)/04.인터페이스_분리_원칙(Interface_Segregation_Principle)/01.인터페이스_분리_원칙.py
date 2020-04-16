"""
인터페이스란?
파이썬에는 없는 개념이긴 하지만 추상 클래스 중에서 추상 메소드만 있고 일반 메소드는 없는 것!

인터페이스 분리 원칙
클래스가 사용하지 않을 메소드에 의존할 것을 강요하면 안 된다.
=> 클래스가 나중에 사용하지도 않을 메소드를 가지도록 강제하지 말라는 뜻!

추상 클래스를 상속 받으면 자식 클래스는 추상 메소드를을 반드시 오버라이딩해야 한다.

추상클래스를 인터페이스라고 부른다.
"""

from abc import ABC, abstractmethod


class IMessage(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass

    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass


class Email(IMessage):
    def __init__(self, content, owner_email):
        """이메일은 그 내용과 보낸 사람의 이메일 주소를 인스턴스 변수로 가짐"""
        self._content = content
        self.owner_email = owner_email

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """이메일 내용 수정 메소드"""
        self._content = self.owner_email + "님의 메일\n" + new_content

    def send(self, destination):
        """이메일 전송 메소드"""
        print("{}에서 {}로 이메일 전송!\n내용: {}").format(self.owner_email, destination, self._content)
        return True


class TextMessage(IMessage):
    def __init__(self, content):
        """문자 메시지는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """_content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """문자 메시지 내용 수정 메소드"""
        self._content = new_content

    def send(self, destination):
        """문자 메시지 전송 메소드"""
        print("{}로 문자 메시지 전송!\n내용: {}").format(destination, self._content)


class TextReader:
    """인스턴스의 텍스트 내용을 읽어주는 클래스"""

    def __init__(self):
        self.texts = []

    def add_text(self, text: IMessage): # message지는 IMessage를 상속 받은 인스턴스여야 한다는 뜻
        """인스턴스 추가 메소드, 파라미터는 IMessage 인터페이스를 상속받을 것"""
        self.texts.append(text)

    def read_all_texts(self):
        """인스턴스 안에 있는 모든 텍스트 내용 출력"""
        for text in self.texts:
            print(text.content)

# Memo 클래스가 IMessage 상속하는데 send 메소드를 사용하지 않는데 억지로 오버라이딩 하였으므로, 인터페이스 분리 원칙 위반
# IMessage처럼 너무 많은 메소드를 한번에 갖고 있는 인터페이스를 뚱뚱한 인터페이스라고 한다. 더 작은 인터페이스로
# 나눠주어 인터페이스 분리 원칙 위반하지 않을려고 해야 한다.
class Memo(IMessage):
    def __init__(self, content):
        """메모는 그 내용을 인스턴스 변수로 가짐"""
        self._content = content

    @property
    def content(self):
        """content 변수 getter 메소드"""
        return self._content

    def edit_content(self, new_content):
        """메모 내용 수정 메소드"""
        self._content = new_content

    def send(self, destination):
        """메모는 전송할 수 없음"""
        print("메모는 아무 데도 보낼 수 없습니다!")
        return False

email = Email("안녕 잘 지내니? 오랜만이다!", "young@codeit.kr")
text_message = TextMessage("내일 시간 가능? 한 1시쯤 만나자")
memo = Memo("내일 2시까지 숙제 끝낼 것!")

text_reader = TextReader()

text_reader.add_text(email)
text_reader.add_text(text_message)
text_reader.add_text(memo)

text_reader.read_all_texts()

"""인터페이스 분리 원칙
클래스가 사용하지 않을 메소드에 의존할 것을 강요하면 안 된다.
* 의존 -> 의존한다는 표현은 메소드를 갖는다는 것!"""
