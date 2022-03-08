class Animal:
    def __init__(self,age):
        self.age = age
        print('Animal 생성자 호출')

    def print_info(self):
        print('이 동물의 나이 : {}'.format(self.age))

class Person(Animal):
    #자식 생성자는 부모 클래스 생성에 필요한 데이터를 받아서 보내줘야됨
    def __init__(self,age,name):
        super().__init__(age)
        self.name = name
        print('Person 생성자 호출')

    def print_info(self):
        print('이름 : {}'.format(self.name))
        super().print_info()#부모클래스에 생성된 메서드 호출
p = Person(20,"홍길동")
p.print_info()