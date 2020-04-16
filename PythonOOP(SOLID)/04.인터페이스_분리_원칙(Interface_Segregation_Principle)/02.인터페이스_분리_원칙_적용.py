# Memo 클래스가 IMessage 상속하는데 send 메소드를 사용하지 않는데 억지로 오버라이딩 하였으므로, 인터페이스 분리 원칙 위반
# IMessage처럼 너무 많은 메소드를 한번에 갖고 있는 인터페이스를 뚱뚱한 인터페이스라고 한다. 더 작은 인터페이스로
# 나눠주어 인터페이스 분리 원칙 위반하지 않을려고 해야 한다.
# 이것을 역할 인터페이스(role interface)라고 한다.

from abc import ABC, abstractmethod


class IText(ABC):
    @property
    @abstractmethod
    def content(self):
        """추상 getter 메소드"""
        pass

    @abstractmethod
    def edit_content(self, new_content: str) -> None:
        """작성한 메시지를 수정하는 메소드"""
        pass


class ISendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> bool:
        """작성한 메시지를 전송하는 메소드"""
        pass



class Email(IText, ISendable):
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


class TextMessage(IText, ISendable):
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

class Memo(IText):
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


# Memo 클래스가 IMessage 상속하는데 send 메소드를 사용하지 않는데 억지로 오버라이딩 하였으므로, 인터페이스 분리 원칙 위반
# IMessage처럼 너무 많은 메소드를 한번에 갖고 있는 인터페이스를 뚱뚱한 인터페이스라고 한다. 더 작은 인터페이스로
# 나눠주어 인터페이스 분리 원칙 위반하지 않을려고 해야 한다.
class TextReader:
    """인스턴스의 텍스트 내용을 읽어주는 클래스"""

    def __init__(self):
        self.texts = []

    def add_text(self, text: IText): # message지는 IMessage를 상속 받은 인스턴스여야 한다는 뜻
        """인스턴스 추가 메소드, 파라미터는 IMessage 인터페이스를 상속받을 것"""
        self.texts.append(text)

    def read_all_texts(self):
        """인스턴스 안에 있는 모든 텍스트 내용 출력"""
        for text in self.texts:
            print(text.content)


email = Email("안녕 잘 지내니? 오랜만이다!", "young@codeit.kr")
text_message = TextMessage("내일 시간 가능? 한 1시쯤 만나자")
memo = Memo("내일 2시까지 숙제 끝낼 것!")

text_reader = TextReader()

text_reader.add_text(email)
text_reader.add_text(text_message)
text_reader.add_text(memo)

text_reader.read_all_texts()

"""인터페이스를 분리할 때 더 분리할 수 있을지 여부를 항상 고민해야 합니다.
인터페이스를 어떤 기준으로 분리할 수 있다면  인터페이스가 더 분리할 수 있는 것 입니다.
무조건 쪼개라는 것은 아니다. 어떤 기능과 역할이 있을 때 분리되는 수준으로 나누면 됩니다."""

# 정리
"""이번 시간에 배운 인터페이스 분리 원칙(Interface Segregation Principle)을 정리해보겠습니다.


이 원칙은 지나치게 많은 추상 메소드를 가진 거대한 인터페이스 하나를, 관련된 추상 메소드들만 모여있도록 작은 크기의 
인터페이스로 분리하라는 뜻입니다. 이렇게 해야 하는 이유는 지나치게 큰 인터페이스는 그걸 상속하는 클래스가 자신에게 
필요하지도 않은 메소드를 굳이 오버라이딩하도록 만들기 때문입니다.


인터페이스가 서로 관련성이 높은, 적절한 개수의 추상 메소드들을 포함하게 될 때 그걸 역할 인터페이스(role interface)라고 
하는데요. 큰 인터페이스 하나가 있는 것보다는 작은 역할 인터페이스 여러 개가 있으면 각 클래스가 본인에 해당하는 
인터페이스만 적절히 상속받게 됩니다. 그럼 각 클래스가 어떤 기능을 갖는지 더 세밀하게 파악할 수 있게 해준다는 장점도 있습니다.


인터페이스를 분리할 때 어떤 기준으로 나눌지는 상황에 따라 당연히 다를 겁니다. 하지만 중요한 건 관련있는 기능끼리 
한 인터페이스에 모으고 한 인터페이스가 지나치게 커지지 않도록 하겠다는 생각을 갖고 인터페이스를 설계하는 겁니다."""

# 인터페이스 분리 원칙을 지키지 않는다고 코드 실행에 문제가 생기지는 않습니다. 다만 여러 클래스들이 굳이 갖지 않아도 되는 메소드를 갖게됨으로써 코드가 지저분해지고 전체적인 코드 파악이 힘들어집니다.
# 일반 클래스 또는 일반 메소드가 섞여 있는 추상 클래스들은 되도록 다중 상속을 하지 않는게 좋습니다. 다중 상속을 꼭 해야 하는 경우라면 주의를 기울여서 해야 하구요. 하지만 일반 메소드가 없고, 추상 메소드로만 이루어진 인터페이스는 다중 상속을 해도 됩니다. 어차피 자식 클래스에서 추상 메소드를 오버라이딩해야하기 때문에 다중 상속을 할 때 발생하는 "어떤 부모 클래스의 메소드를 호출하는지를 매번 확인해야 하는 문제"가 발생할 일이 없기 때문입니다. 오히려 하나의 거대한 인터페이스를 작은 역할 인터페이스 여러 개로 쪼개서 이것들을 다중 상속받는 게 인터페이스 분리 원칙을 지키는 방법입니다.
