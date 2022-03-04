'''
    총(Gun) 클래스
        field
            총알 - 정수
        method
            생성자 : 총알 값을 12로 초기화
            발사 : 총알이 1발씩 감소 --> BBang! 출력
                   총알이 없으면 --> reload! 출력
                   총알을 12발 리필
            재장전 : 총알을 12발 리필
'''
class Gun:
    def __init__(self):
        self.__bullet = 12
    def shot(self):
        if self.__bullet == 0:
            self.reload()
        else:
            self.__bullet -= 1
            print("BBang!!")
    def reload(self):
        self.__bullet = 12
        print("reload!!")

gun = Gun()
for i in range(20):
    gun.shot()




