"""다음은 코드잇 대학의 학생 관리 프로그램에서 사용되는 학생(Student) 클래스입니다. 학생 클래스에는

학생 기본 정보 수정
학점 추가
평균 학점 계산
성적표 출력"

기능들이 있습니다. 그런데 학생 클래스는 너무 많은 책임을 갖고 있는 신 객체(God object)에 해당합니다.
학생 클래스를 단일 책임 원칙에 맞게 바꿔보세요. 책임을 나누는 방식은 다양할 수 있습니다.
일단은 여러분이 생각하는 기준으로 책임을 나눠서 과제를 풀어보세요. 그 다음 해설을 참고로 보시기 바랍니다."""


class Student:
    def __init__(self, name, id, major, grade):
        self.name_book = NameBook(name)
        self.id_card = IdentificationCard(id)
        self.major_list = MajorList(major)
        self.grades = GradeManager(grade)


class NameBook:
    def __init__(self, name):
        self.name = name

    def change_student_info(self, new_name):
        """학생 기본 정보 수정 메소드"""
        self.new_name = new_name

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("코드잇 대학 성적표\n\n학생 이름:{}".format(self.name))


class IdentificationCard:
    def __init__(self, id):
        self.id = id

    def change_student_info(self, new_id):
        """학생 기본 정보 수정 메소드"""
        self.new_id = new_id

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("학생 번호:{}".format(self.new_id))


class MajorList:
    def __init__(self, major):
        self.major = major

    def change_student_info(self, new_major):
        """학생 기본 정보 수정 메소드"""
        self.major = new_major

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("소속 학과:{}".format(self.major))


class GradeManager:
    def __init__(self, grade):
        self.grades = grade

    def add_grade(self, grades):
        """학점 추가 메소드"""
        if 0 <= grades <= 4.3:
            self.grades.append(grades)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

    def get_average_gpa(self):
        """평균 학점 계산 메소드"""
        return sum(self.grades) / len(self.grades)

    def print_report_card(self):
        """학생 성적표 출력 메소드"""
        print("평균 학점:{}".format(self.get_average_gpa()))


# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과", [])
younghoon.name_book.change_student_info("강영훈")
younghoon.id_card.change_student_info(20130024)
younghoon.major_list.change_student_info("컴퓨터 공학과")

# 학생 성적 추가
younghoon.grades.add_grade(3.0)
younghoon.grades.add_grade(3.33)
younghoon.grades.add_grade(3.67)
younghoon.grades.add_grade(4.3)

# 학생 성적표
younghoon.name_book.print_report_card()
younghoon.id_card.print_report_card()
younghoon.major_list.print_report_card()
younghoon.grades.print_report_card()
