class DeliveryMan:
    """배달원 클래스"""
    company_name = "코드잇 버거"   # 가게 이름
    raise_percentage = 1.03        # 시급 인상률
    # 클래스 변수

    def __init__(self, name, wage, on_standby):
        #인스턴스 메소드
        self.name = name        # 이름
        self.wage = wage        # 시급
        self.on_standy = on_standby     # 하루 판매량
        # 인스턴스 변수

    def raise_pay(self):
        #인스턴스 메소드
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def take_order(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 설명 메시지를 출력한다"""
        if self.on_standy:
            print(address + "로 배달 나갑니다!")
            self.on_standy = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원을 복귀 처리한다"""
        self.on_standy = True

    def __str__(self):
        #인스턴스 메소드
        return DeliveryMan.company_name + " 배달원: " + self.name
