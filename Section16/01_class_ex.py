'''
    TV
        field
            전원 - true/false
            채널 - 정수 : 1 ~ 455
            음량 - 정수 : 0 ~ 50
        method
            init --> 전원, 채널, 음량 필드를 선언하고 초기화하는 메서드
            채널Up --> 실행 할때마다 채널 값을 증가, 마지막 채널값에서 증가하면 처음 채널로 이동
'''
class TV:
    def init(self):
        # self.__변수 --> private 멤버 --> 클래스 내부에서만 접근이 가능
        # self.변수 --> public 멤버 --> 누구든지 접근이 가능
        self.__power = False
        self.__ch = 24
        self.__vol = 15

    def ch_up(self):
        self.__ch += 1
        if self.__ch > 455:
            self.__ch = 1
        print(f'현재 채널 : {self.__ch}')

tv = TV()
tv.init()
for i in range(500):
    tv.ch_up()
#print(tv.__ch)



