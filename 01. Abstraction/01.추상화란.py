# 프로그래밍에서 추상화란?
# 프로그래머들이 특정 코드를 사용할 때 필수적인 정보를 제외한 세부사항을 가리는 것 / ex. coffee machine

# 변수나 함수를 작성하는 것도 추상화이다.
# 값을 몰라도 변수명만 알아도 되기 때문이다.
# 우사인 볼트의 평균 속도 = 10.438413361 m / s
bolt_speed = 10.438413361
minute = 60

print(bolt_speed * minute)      # 1분(60초) 동안 간 거리
print(bolt_speed * 2 * minute)      # 2분(120초) 동안 간 거리
print(bolt_speed * 3 * minute)      # 3분(180초) 동안 간 거리

# 함수 추상화
# 함수의 이름과 파라미터, 무엇을 하는지 알면 사용할 수 있기 때문에 추상화이다.
def welcome(name):
    print("Hello, " + name)
    print("Welcome to Codeit!")


welcome("영훈")
welcome("규식")
welcome("대위")


# []를 이용해서 빈 리스트 인스턴스를 정의한다.
example_list = []
example_list.append(3)
example_list.append(2)
example_list.append(6)
print(example_list[0])
print(example_list[1])
print(example_list[2])
