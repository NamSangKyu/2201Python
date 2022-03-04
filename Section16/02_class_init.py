'''
    생성자(Constructor) 
        객체를 생성할 때 제일 먼저, 단 한번만 실행되는 메서드 
'''
class Person:
    def __init__(self):
        print("Person 생성자")
        self.name = "홍길동"
        self.age = 20
    def print_info(self):
        print(f'{self.name} - {self.age}')

p1 = Person()
p2 = Person()
p3 = Person()
p1.print_info()
p2.print_info()
p3.print_info()

class Animal:
    def __init__(self, age):
        self.age = age

    def print_info(self):
        print(f'이 동물의 나이 : {self.age}')

animal = Animal(20)
# animal = Animal() 생성자에 매개변수가 있으면 반드시 해당하는 데이터를 넣어야됨
animal.print_info()






