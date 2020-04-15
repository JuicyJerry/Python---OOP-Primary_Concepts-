# Open/closed priciple
"""클래스는 확장에 열려 있어야하며, 수정에는 닫혀있어야한다.
= 확장에 열려 있다는 건 프로그램의 기존 기능을 확장할 수 있다는 것이고
수정에 닫혀 있다는 건 한 번 작성한 코드를 바꾸지 않아도 되는 것입니다."""

""" 새로운 키보드가 등장할 때마다 keyboardManager를 수정하는 것은 개방 폐쇄 원칙에 위반한다.
왜냐하면 개방 폐쇄 원칙에 의하면, 새로운 키보드가 추가 되어도 코드는 수정되지 않아야하기 때문이다.

기존 클래스의 코드를 수정하지 않고도 기능을 확장할 수 있어야 한다는 뜻 = 추상 클래스(abstract class)를 사용함
1. 개방-폐쇄 원칙을 적용했던 KeyboardManager 클래스는 내부에서 사용할 인스턴스를 Keyboard라는 추상 클래스의 (자식 클래스의) 인스턴스로 제한했습니다.
2. 그리고 다양한 종류의 키보드 클래스는 Keyboard 추상 클래스를 상속받도록 했죠.

그러니까 KeyboardManager 클래스에는 Keyboard 추상 클래스의 자식 클래스의 인스턴스만 들어갈 수 있다는 제한이 생겼고,
그럼 KeyboardManager 클래스는, 그 인스턴스가 Keyboard 추상 클래스의 메소드를 오버라이딩해서 갖고 있을 것이라고 믿고 
사용할 수 있습니다.

만약 이런 제한이 없다면 KeyboardManager 클래스에 키보드로 어떤 클래스의 인스턴스가 들어올지 모릅니다. 
이렇게 되면 새로운 종류의 키보드가 생길 때마다 그것에 맞게 KeyboardManager 클래스를 수정해야 합니다. 
왜냐하면 인스턴스가 어떤 클래스의 것인지를 매번 isinstance 함수로 체크해서 그 클래스가 갖고 있는 메소드를 
호출해야 하기 때문입니다. 이건 그만큼 프로그램의 유지보수가 힘들어진다는 뜻입니다.
"""

from abc import ABC, abstractmethod

class Keyboard(ABC):
    """키보드 (추상)클래스"""
    def save_input(self, content: str) -> None:
        """키보드 인풋 저장 메소드!"""
        pass

    @abstractmethod
    def send_input(self) -> str:
        """키보드 인풋 전송 메소드"""
        pass
    # 모든 키보드 클래스는 keyboard 추상 클래스를 상속받는다.


class AppleKeyboard(Keyboard):
    """애플 키보드 클래스"""
    def __init__(self):
        """키보드 인풋과 터치바 인풋"""
        self.keyboard_input = input

    def save_input(self, input):
        """키보드 인풋 설정 메소드"""
        self.keyboard_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.keyboard_input


class SamsungKeyboard(Keyboard):
    """삼성 키보드 클래스"""
    def __init__(self):
        """키보드 인풋"""
        self.user_input = ""

    def save_input(self, input):
        """키보드 인풋 저장 메소드"""
        self.user_input = input

    def send_input(self):
        """키보드 인풋 전송 메소드"""
        return self.user_input


class KeyboardManager:
    def __init__(self):
        """키보드 관리 클래스"""
        self.keyboard = None

    def connect_to_keyboard(self, keyboard):
        """키보드 교체 메소드"""
        self.keyboard = keyboard

    def get_keyboard_input(self):
        """유저가 키보드로 입력한 내용을 받아오는 메소드"""
        return self.keyboard.send_input()

keyboard_manager = KeyboardManager()

apple_keyboard = AppleKeyboard()
samsung_keyboard = SamsungKeyboard()

keyboard_manager.connect_to_keyboard(apple_keyboard)
apple_keyboard.save_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())

keyboard_manager.connect_to_keyboard(samsung_keyboard)
samsung_keyboard.save_input("안녕하세요")
print(keyboard_manager.get_keyboard_input())

"""
Class Keyboard Manager(추상 클래스): 개방 폐쇄 원칙 - 확장 O, 수정: X (수정할 필요 없어요!)
이 때 연결하는 키보드는 어떤 키보드이던 연결할 수 있다(<-> 동시에 추상 클래스의 상속받는다). => 변수 keyboard는 다형성을 갖는다. => 개방 폐쇄 원칙을 지키게 된다.

또한, 개방 폐쇄 원칙을 사용하는 게 isinstance 사용하는 것보다 바람직하다.
왜냐하면, 개방 폐쇄 원칙이 개발의 편의성과 코드의 유지보수성을 높여주기 때문이다.
예를 들어, 개방 폐쇄 원칙은 동시에 어떤 사람이 코드를 작성하더라도 추상 클래스를 이용하게 되면 동시에 개발이 가능하다.
하지만, isinstance를 사용하게 되면 키보드 클래스를 추가할 때마다 isinstance를 추가해줘야 되기 때문에 전자가 더 낫다고 한다.

개방 폐쇄 원칙을 지키는 이유 => 더 쉽게 협력하고 더 편하게 수정하기 위해서!
"""
