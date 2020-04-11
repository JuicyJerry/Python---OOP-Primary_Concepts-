from math import pi

class Rectange:
    """직사각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2*self.width*2*self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)


class Circle:
    """원클래스"""
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
        return "반지를 {}인 원".format(self.radius)

class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []
        # shape가 Rectangle 인스턴스 or Circle 인스턴스 -> 다양성이라고 한다
        # shape 메소드에 Rectagle, Circle 클래스가 area(), perimeter() 메소드가 있기 때문에 가능한 것이다.

    def add_shape(self, shape):
        """그림판에 도형을 추가한다"""
        self.shapes.append(shape)

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])
        # list comprehension

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다."""
        return sum([shape.perimeter() for shape in self.shapes])


    def __str__ (self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str

rectangle = Rectange(3, 7)
circle = Circle(4)

paint_program = Paint()
paint_program.add_shape(rectangle)
paint_program.add_shape(circle)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())

# 다형성: 여러가지 성질을 갖는 인스턴스
# 변수 -> A 클래스의 인스턴스
# 변수 -> B 클래스의 인스턴스

