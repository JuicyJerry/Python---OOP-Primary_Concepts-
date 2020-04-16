"""자식 클래스가 부모 클래스의 의도와 다르게 메소드를 오버라이딩 하는 경우"""

class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1

#1.
#class Square(Rectangle):
#    def __init__(self, side):
#        super().__init__(side, side)
"""근데 스퀘어 이렇게 되면 rectangle_2.width, height가 정삼각형인데 가로와 세로의 길이가 달라지는 상황이 되버립니다.
실제로 정삼각형은 가로, 세로 길이가 같아야 하는게 정의이다.
 
이런 상황에서는 어떻게 할까요?
square에서 정삼각형 원칙에 맞게 오버라이딩하니깐 리스코프 치환 원칙을 어기게 되고, 
오버라이딩을 하지 않으니깐 정삼각형 원칙에 위배되는 상황이 되버림

여기서, 
정사각형은 직사각형 행동규약을 지키기 어려움 그래서 아예 직사각형을 상속하면 안 된다.

"A는 B다." 라는 상속관계가 형성되는 거 더해서, "A가 B의 행동규약을 지키는가" 도 보아야 상속관계를 설정해도 문제 없다.
"""
#2.


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        """정사각형 넓이 계산 메소드"""
        return self.side * self.side

    @property
    def side(self):
        """한 번 getter 메소드"""
        return self._side

    @side.getter
    def side(self, value):
        """한 변 setter 메소드"""
        self._side = value if value > 0 else 1

retangle_1 = Rectangle(4, 6)

#1. retangle_2 = Square(2)
#2.

square = Square(2)

retangle_1.width = 3
retangle_1.height = 7

print(retangle_1.area())

square.side = 10

print(square.area())
