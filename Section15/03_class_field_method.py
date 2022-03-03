'''
    field : 클래스에서 변수에 해당
    method : 클래스에서 함수에 해당
Person 클래스에서 이름, 나이를 저장하고
이름과 나이를 출력하는 print_person_info 메서드를 작성
'''
class Person:
    #self : 현재 생성된 객체
    def setting_data(self, name, age):
        #현재 객체에 name 변수와 age 변수를 선언하고 매개변수로 받은 name, age를 필드에 저장
        self.name = name
        self.age = age
    def print_person_info(self):
        print(f'{self.name} - {self.age}')

person1 = Person()
person1.setting_data('홍길동',20)
person1.print_person_info()


person2 = Person()
person2.setting_data('김철수',30)
person2.print_person_info()




