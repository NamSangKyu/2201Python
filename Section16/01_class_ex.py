'''
    TV
        field
            전원 - True(On)/False(Off)
            채널 - 정수 : 1 ~ 455
            음량 - 정수 : 0 ~ 50
        method
            init --> 전원, 채널, 음량 필드를 선언하고 초기화하는 메서드
            채널Up --> 실행 할때마다 채널 값을 증가, 마지막 채널값에서 증가하면 처음 채널로 이동
            채널Down --> 실행 할때마다 채널 값을 감소, 처음 채널에서 감소하면 마지막 채널로 이동
            음량Up --> 실행 할때마다 음량 값을 증가, 최대 음량에서는 더이상 증가가 안됨
            음량Down --> 실행 할때마다 음량 값을 감소, 최소 음량에서는 더이상 감소가 안됨
            전원OnOff --> 실행 할때마다 켜져 있으면 끄고, 꺼져 있으면 켜기
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

    def ch_down(self):
        self.__ch -= 1
        if self.__ch < 1:
            self.__ch = 455
        print(f'현재 채널 : {self.__ch}')

    def vol_up(self):
        if self.__vol < 50:
            self.__vol += 1
        print(f'현재 음량 : {self.__vol}')

    def vol_up(self):
        if self.__vol > 0:
            self.__vol -= 1
        print(f'현재 음량 : {self.__vol}')

    def power_on_off(self):
        #True --> False, False --> True
        self.__power = not self.__power
        if self.__power:
            print('TV 전원 On')
        else:
            print('TV 전원 Off')
tv = TV()
tv.init()
tv.power_on_off()
tv.power_on_off()
tv.power_on_off()
tv.power_on_off()
# for i in range(500):
#     tv.ch_up()
#print(tv.__ch)
# for i in range(50):
#     tv.ch_down()



