# 1. 추상 클래스와 추상화!
"""우리는 지금 “객체 지향 프로그래밍의 4가지 기둥” 중 마지막에 해당하는 “다형성”을 배우고 있습니다.
시 첫 번째로 배웠던 “추상화” 기억나시나요? 추상화는 변수, 함수, 클래스를 사용해 사용자가 꼭 알아야만 하는 부분만
겉으로 드러내는 것이라고 배웠습니다. 이번에 배운 추상 클래스도 이러한 추상화의 한 예시입니다.
추상 클래스는 서로 관련있는 클래스들의 공통 부분을 묶어서 추상화합니다."""


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 문자열로 리턴한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


"""Paint 클래스를 사용하는 개발자는 add_shape 메소드에서 파라미터 shape으로 들어오는 인스턴스의 타입이 Shape 클래스일 
때만 그 인스턴스를 추가합니다. 이는 해당 인스턴스가 구체적으로 무슨 도형의 인스턴스인지는 관심이 없고 Shape 클래스의 
인스턴스에만 해당하면 된다는 뜻입니다. 여기서 Shape 클래스는 추상 클래스입니다. 따라서 Shape 클래스의 인스턴스라는 것은 
그 인스턴스의 클래스가 Shape 클래스를 상속받은 자식 클래스로, 추상 메소드 area와 perimeter를 오버라이딩한 클래스여야
한다는 뜻이죠. 정리하자면 도형을 나타내는 클래스라면 가질 수 밖에 없는 공통점을 Shape 클래스로 추상화한 것입니다.
이렇게 하면 Paint 클래스의 코드를 작성하는 개발자는 추상 클래스로 추상화된 수준(Shape 클래스)까지만 고려하고 개발을 
진행할 수 있습니다. 그러니까 개발자는 추가된 각 도형 인스턴스가 구체적으로 무슨 클래스의 인스턴스인지 확인할 필요없이, 
일단 area, perimeter 메소드를 가지는 인스턴스라고 생각하고 개발할 수 있는 것이죠. 이 상황에서 좀더 추가하자면
 add_shape 메소드에 Shape 타입을 가지는 인스턴스가 shape 파라미터로 들어와야 한다는 것을 알려주기 위해 다음과 같이 
 파이썬의 type hinting 기능을 사용할 수 있습니다.

def add_shape(self, shape: Shape):

이런 type hinting 자체만으로 Shape 클래스의 인스턴스만 들어오도록 강제할 수는 없지만, 이런 정보를 둬야 개발자가 Paint 
클래스를 제대로 사용할 수 있겠죠?
"""

# 2. 추상 클래스에도 일반 메소드를 추가할 수 있어요!
"""추상 클래스에 꼭 추상 메소드만 있어야하는 것은 아닙니다. @abstractmethod 데코레이터가 없는 일반적인 메소드가 있어도 
상관없습니다. 이 메소드들 또한 자식 클래스가 물려받아 그대로 사용하거나 오버라이딩하여 사용할 수 있습니다. 다음 예시를 봅시다."""
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    def larger_than(self, shape):
        """해당 인스턴스의 넓이가 파라미터 인스턴스의 넓이보다 큰지를 불린으로 나타낸다"""
        return self.area() > shape.area()
"""Shape 클래스 중 larger_than 메소드가 일반 메소드입니다. 이 메소드는 파라미터로 전달된 다른 도형 인스턴스의 넓이와 자신의 넓이를 비교합니다.
Shape 클래스를 상속받는 원(Circle) 클래스를 만들고 원 인스턴스로 일반 메소드 larger_than을 호출해보면"""
class Circle(Shape):
    """원 클래스"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

circle = Circle(6)
rectangle = Rectangle(3, 4)
print(circle.larger_than(rectangle)) # 출력: True
"""제대로 작동합니다.  즉, 추상 클래스에는 꼭 추상 메소드뿐만 아니라 일반 메소드도 정의할 수 있고 이것도 똑같이 
자식 클래스가 물려받습니다. 하지만 차이점이 있다면 
1. 반드시 오버라이딩해야하는 추상 메소드와 달리 
2. 일반 메소드는 물려받은 그대로 사용할지, 오버라이딩할지를 자식 클래스에서 결정하는 것이구요."""

# 3. 추상 메소드에도 내용을 채울 수 있습니다!
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass


""" 지금까지는 추상 메소드의 내용으로 그냥 pass만 써줬습니다. 하지만 사실 추상 메소드 안에는 다른 내용을 써도 됩니다. 
아래 코드처럼요!"""

from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형의 넓이 계산 중!")   # ---------------- 추가된 코드

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

"""그런데 좀 이상하죠? 어차피 추상 클래스를 상속받는 자식 클래스에서 이 추상 메소드들은 반드시 오버라이딩해야 합니다. 
그래서 이렇게 어차피 무시될 추상 메소드의 내용이 왜 필요한지 모르겠군요.
하지만 사실 이 내용은 경우에 따라 유용할 때가 있습니다. 보통 추상 메소드에 내용을 쓸 때는 모든 자식 클래스에 
해당하는 공통 내용을 써줍니다. 그리고 자식 클래스에서 추상 메소드를 오버라이딩하더라도 이렇게 미리 채워진 내용을 
가져와서 재활용할 수 있습니다. 이는 super 함수를 사용하면 가능합니다."""
class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        super().area() # ---------------- 부모의 메소드를 가져다 씀
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2*self.width + 2*self.height


rectangle = Rectangle(3, 4)
print(rectangle.area())# 출력: 도형의 넓이 계산 중! 12

"""예전에 부모 클래스의 __init__ 메소드를 사용할 때 자식 클래스에서 super 함수로 부모 클래스의 내용에 접근할 수 있다고 
설명한 적이 있는데 혹시 기억하시나요? super 함수를 사용하면 부모 클래스에 접근할 수 있습니다. 이 코드 중 area 메소드를 
보세요. 부모 클래스인 Shape 클래스의 area 메소드를 실행하는 부분이 있습니다.

즉, 물려받은 추상 메소드를 오버라이딩하는데 super 함수를 통해 추상 메소드의 기존 내용(print("도형 넓이 계산 중!"))을 
포함함과 동시에 이와 별도로 자신만의 내용을 또 추가한거죠.(return self.width * self.height)

이렇게 모든 자식 클래스에서 공통적으로 사용할 부분을 추상 메소드의 내용으로 써주고 자식 클래스에서 이를 super 함수로 
접근하는 방법은 꽤 자주 쓰는 방법입니다. 이번 기회에 꼭 기억하세요!"""

# 4. 자식 클래스가 특정 변수를 갖도록 유도할 수 있어요!
"""추상 클래스를 사용하면 자식 클래스가 추상 클래스의 추상 메소드를 오버라이딩하도록 즉, 해당 메소드를 갖도록 강제할 
수 있습니다. 하지만 이밖에도 추상 클래스로 자식 클래스가 특정 변수를 갖도록 유도할 수 있는 방법이 있습니다. 
예시를 통해 알아볼까요? 이 부분이 이 노트의 4가지 내용 중 가장 어려운데요, 하나씩 살펴봅시다.

그림판에서 사용할 모든 도형 클래스는 좌표를 나타내는 인스턴스 변수 x와 y를 반드시 가져야한다고 가정합시다. 
어떻게 하면 추상 클래스를 사용해 각 자식 클래스가 이 변수를 갖도록 유도할 수 있을까요?"""
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        print("도형 넓이 계산 중!")

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다: 자식 클래스가 오버라이딩할 것"""
        pass

    def __str__(self):
        return "추상 클래스라고 해서 모든 메소드가 추상 메소드일 필요는 없습니다!"

    @property
    @abstractmethod
    def x(self):
        """도형의 x 좌표 getter 메소드"""
        pass

    @property
    @abstractmethod
    def y(self):
        """도형의 y 좌표 getter 메소드"""
        pass

"""위 코드를 보세요.  이 Shape 클래스는 지금 x 메소드와 y 메소드를 getter 메소드이자 추상 메소드로 갖고 있습니다. 
@property는 파이썬스럽게 getter/setter 메소드를 정의하는 방법에서 배웠던 데코레이터입니다. 기억나시죠?

이렇게 @property 와 @abstractmethod 데코레이터를 메소드 이름 위에 연달아 적어주면 이 메소드는 getter 메소드이자 
추상 메소드가 됩니다. 즉, 어떤 변수에 대한 getter 메소드를 뜻하지만 아직 내용이 비어있어 어떤 변수를 리턴하는지는 
결정되지 않은 것이죠. 이때 Shape 클래스를 상속받는 자식 클래스에서 어떤 변수를 리턴하는지 즉, 이 getter 메소드가 
어떤 변수에 대한 것인지를 나타내도록 오버라이딩해야하는 것입니다.

일단 Shape 클래스를 상속받는 정삼각형 클래스인 EquilateralTriangle 클래스를 정의했습니다. getter 메소드들을 
오버라이딩하지 않으면 다음과 같은 에러가 뜹니다.
"""

class EquilateralTriangle(Shape):
    """정삼각형을 나타내는 클래스"""
    def __init__(self, side):
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side

equilateral_triangle = EquilateralTriangle(4) # 에러 발생: TypeError: Can't instantiate abstract class EquilateralTriangle with abstract methods x, y

"""추상 메소드 x, y를 오버라이딩하지 않아서 생긴 에러입니다.
그렇다면 각 getter 메소드는 어떻게 오버라이딩하면 될까요? 
보통 인스턴스 변수의 이름은 예를 들어 _apple 처럼 캡슐화를 적용한 것으로 나타내고 getter 메소드의 이름은 apple 처럼 
캡슐화된 변수 이름 앞에서 밑줄을 뺀 이름으로 한다고 배웠습니다. 이 경우에 적용한다면 x는 인스턴스 변수 _x의 getter 
메소드로, y는 인스턴스 변수  _y의 getter 메소드로 해주면 좋을 것 같네요."""
@property
    def x(self):
        """_x getter 메소드"""
        return self._x

@x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

"""혹시 @property 데코레이터의 기능이 잘 생각나지 않는 분을 위해 설명하자면 
이 코드의 의미는 이 클래스의 인스턴스에 대해 self.x , 인스턴스 이름.x 와 같은 부분을 실행할 때, getter 메소드 x를 
실행한다는 의미입니다. 즉, @property가 붙으면 이런 구문들이 인스턴스 변수 x의 값을 직접 읽는다는 원래의 뜻이 아니라 
getter 메소드 x를 실행한다는 의미로 바뀌는 거죠. 그 아래의 @x.setter 가 붙은 메소드는 이 클래스의 인스턴스에 대해
self.x = 3 , 인스턴스 이름.x = 3 과 같은 부분을 실행할 때 setter 메소드 x를 실행한다는 의미입니다. 
즉, @x.setter가 붙으면 이런 구문들이 인스턴스 변수 x에 어떤 값을 설정한다는 원래의 뜻이 아니라 setter 메소드 x를 
실행한다는 의미로 바뀌는 것이구요.

그럼 이때까지 설명한 조건에 부합하는 EquilateralTriangle 클래스를 완성한 결과를 봅시다."""

class EquilateralTriangle(Shape):
     """정삼각형 클래스"""
    def __init__(self, x, y, side):
        self._x = x
        self._y = y
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side

    @property
    def x(self):
        """_x getter 메소드"""
        return self._x

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

    @property
    def y(self):
        """_y getter 메소드"""
        return self._y

    @y.setter
    def y(self, value):
        """_y setter 메소드"""
        self._y = value

equilateral_triangle = EquilateralTriangle(5, 6, 4) # 에러가 나지 않는다
equilateral_triangle.x = 10
print(equilateral_triangle.x) # 출력: 10

equilateral_triangle.y = 5
print(equilateral_triangle.y) # 출력: 5

"""이 코드는 잘 실행됩니다.  물론 Shape 클래스에서 자식 클래스에 getter 메소드를 오버라이딩하도록 강제한다고 해도 자식 
클래스에서 이 메소드를 변수의 내용을 가져오는 getter 메소드로서의 내용이 아닌 아예 엉뚱한 내용으로 오버라이딩할 수도 
있습니다. 하지만 파이썬의 문화를 잘 따르는 개발자라면 getter/setter 메소드의 내용이 되도록 오버라이딩할 것입니다. 
이처럼 부모 클래스에서 추상 메소드인 getter 메소드를 만들어서 자식 클래스가 그 getter 메소드의 대상이 되는 인스턴스 
변수를 갖도록 유도할 수 있는 것입니다!"""
