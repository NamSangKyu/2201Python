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
