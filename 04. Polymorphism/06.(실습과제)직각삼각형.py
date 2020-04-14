"""추상 클래스 Shape 클래스를 상속받는 도형 클래스의 인스턴스라면 그림판에 추가될 수 있도록 했습니다.
다음 조건을 만족하면서, 그림판에 추가될 수 있는 직각삼각형(RightTriangle) 클래스를 만들어봅시다.

직각삼각형(RightTriangle) 클래스의 조건
인스턴스 변수로 밑변(base)과 높이(height)를 갖습니다.
넓이(area)는 밑변 * 높이 / 2 입니다.
둘레(perimeter)는 root (밑변**2 + 높이 **2 + 밑변 + 높이) 입니다."""
from math import sqrt
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


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        """도형 인스턴스만 그림판에 추가한다"""
        if isinstance(shape, Shape):    #LNYL(Look Before Your Leap) <> EAFP(Easier to Ask for Forgiveness than Pemission)
            self.shapes.append(shape)
        else:
            print("도형 클래스가 아닌 인스턴스는 추가할 수 없습니다!")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        return sum([shape.perimeter() for shape in self.shapes])


class RightTriangle(Shape):
    """직각삼각형 클래스"""
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self) -> float:
        """넓이 리턴"""
        return self.base * self.height / 2

    def perimeter(self) -> float:
        """둘레 리턴"""
        return sqrt(self.base ** 2 + self.height ** 2) + self.base + self.height


# 테스트 코드
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

"""직각삼각형(RightTriangle) 인스턴스들은 Shape 클래스의 인스턴스가 맞기 때문에 그림판 프로그램에 잘 추가되는군요. 
추상 메소드도 잘 오버라이딩해서 에러도 나지 않구요. 이렇게 추상 클래스로 원하는 클래스의 조건(여기서는 클래스가 area, 
perimeter 메소드를 가져야한다는 조건)을 정하고 해당 추상 클래스의 인스턴스만 그림판에 추가한다면
(추상 클래스로는 인스턴스를 바로 생성할 수 없으므로 실제로는 해당 추상 클래스의 자식 클래스의 인스턴스입니다, 
isinstance 함수를 배울 때 자식 클래스의 인스턴스는 부모 클래스의 인스턴스이기도 하다는 걸 배웠죠?)
유연하면서도 안전하게 언제든 새로운 종류의 도형을 그림판에 추가할 수 있겠죠?"""
