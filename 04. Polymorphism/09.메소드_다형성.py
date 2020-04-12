# 클래스 다형성
""""변수 -> 인스턴스 A, 인스턴스 B, 인스턴스 C"""
# 함수/메소드 다형성
# 1. 옵셔널 파라미터: 기본 값을 미리 지정해준 파라미터


def new_print(value_1, value_2=None, value_3=None):
    # None: 아무 값도 없다, 함수 호출 시 어떤 파라미터에 값을 전달하지 않은 경우
    # 옵셔널 파라미터는 파라미터 중 가장 뒤에 몰아서 정의(value_2, value_3)
    if value_3 is None:
        if value_2 is None:
            print(value_1)
        else:
            print("{} {}".format(value_1, value_2))
    else:
        print("{} {} {}".format(value_1, value_2, value_3))


new_print("this")   # 출력: this
new_print(0.5678)   # 출력: 0.5678
new_print("this", "that")   # 출력: this that
new_print("this", "that", 3)   # 출력: this that 3

# 2. 파라미터 이름 명시
"""함수를 호출할 때 파라미터 이름 표시"""


def print_name(first_name, last_name, email=""):
    print("{}{} {}".format(last_name, first_name, email))


print_name("태호", "성", "taeho@website.com")   # 출력: 성태호 taeho@website.com
print_name(first_name="태호", last_name="성", email="taeho@website.com")   # 출력: 성태호 taeho@website.com
print_name(email="taeho@website.com", first_name="태호", last_name="성")   # 출력: 성태호 taeho@website.com
print_name(last_name="성", first_name="태호")   # 출력: 성태호 taeho@website.com

# 3. 개수가 확정되지 않은 파라미터
"""마지막 파라미터 이름 앞에*"""


def print_message_and_add_numbers(message, *numbers):
    print(message)
    return sum(numbers)


print(print_message_and_add_numbers("test1", 7, 3, 5))
print(print_message_and_add_numbers("test2", 1, 2, 3, 4, 12))
print(print_message_and_add_numbers("test3", 1, 6, 4, 5))
print(print_message_and_add_numbers("test4", 7))
print(print_message_and_add_numbers("test5", 9, 6))


def print_message_and_add_numbers(*numbers, message):
    print(message)
    return sum(numbers)


print(print_message_and_add_numbers(7, 3, 5, message="test1"))
print(print_message_and_add_numbers(1, 2, 3, 4, 12, message="test2"))
print(print_message_and_add_numbers(1, 6, 4, 5, message="test3"))
print(print_message_and_add_numbers(7, message="test4"))
print(print_message_and_add_numbers(9, 6, message="test5"))

# 함수를 클래스 안으로 옮기면 메소드의 다형성이 되겠죠
# 보통은 클래스 다형성이지만 함수/메소드 다형성도 있다
