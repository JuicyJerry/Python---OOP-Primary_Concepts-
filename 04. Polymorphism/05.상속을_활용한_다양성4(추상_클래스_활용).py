# 원통(Cylinder)클래스
from math import pi, sqrt   # 원주율
from abc import ABC, abstractmethod
# Abstract Base Class
# 추상 메소드가 적어도 1개 이상이 있어야 추상 클래스라고 할 수 있다.


class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    # 추상 메소드: 자식 클래스 오버라이딩 필요 / 인스턴스 생성 x
    def area(self) -> float:
        """도형의 넓이를 리턴한다. 자식 클래스가 오버라이딩할 것"""
        pass

    @abstractmethod
    # 추상 메소드: 자식 클래스 오버라이딩 필요 / 인스턴스 생성 x
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다. 자사 클래스가 오버라이딩할 것"""
        pass


class Rectangle(Shape):
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


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

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class Cylinder:
    """원통 클래스"""

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    """1. ABC 상속, 2. 추상 메소드 -> 추상 클래스 but, 오버라이딩하면 일반클래스를 만들 수 있다"""
    def area(self):
        """원의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 3 * self.side


class Paint:
    """그림판 프로그램 클래스"""

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Shape):
            # 위 코드를 통과하면 에러를 발생시킬 염려가 없다. 이 테스트를 통과한다는 것은
            # 파라미터 shape이 추상 클래스 Shape의 자삭클래스의 인스턴스라는 것이며 area, perimete 메소드를 무조건
            # 가지고 있다는 것이다. => 상속 할 때 부모 클래스를 추상클래스로 만드니깐 더 안전하네요.
            # 클래스가 많아지면 isinstance가 많아진다는 단점이 있다.
            # 하지만 상속이 있다면 isinstance가 하나만 있으면 된다.

            # isinstance(shape, Shape)?
            # =shape은 Shape 클래스의 인스턴스인가?
            # =shape은 area 메소드와 perimeter 메소드를 갖고 있는가?
            self.shapes.append(shape)
        else:
            print("넓이, 둘레를 구하는 메소드가 없는 도형은 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
            return res_str


shape = Shape()

triangle = EquilateralTriangle(4)
paint_program = Paint()
paint_program.add_shape(triangle)

print(paint_program.total_perimeter_of_shapes())
print(paint_program.total_area_of_shapes())

# 추상 클래스
# 여러 클래스들의 공통점을 추상화해서 모아놓은 클래스
