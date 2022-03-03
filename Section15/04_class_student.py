'''
    학생 클래스는 학번, 이름, 학과, 평점을 저장하고 있음
    학생 클래스가 가지고 있는 메서드는
    setting_data를 이용해서 학번, 이름, 학과, 평점을 저장을 하고
    단 평점은 0.0 ~ 4.5일때만 저장, 해당 데이터 범위에 벗어나면 0.0으로 저장
    print_student_info를 이용해서 student 객체가 가지고 있는 내용 아래 형식에 맞게 출력

    20211111    홍길동     컴퓨터공학과      3.45(B)
'''
class Student:
    def setting_data(self,sno,name,major,score):
        self.sno = sno
        self.name = name
        self.major = major
        self.score = 0
        if 0.0 <= score <= 4.5:
            self.score = score

    def get_grade(self):
        if self.score == 4.5:
            return "A+"
        elif 4.0 <= self.score < 4.5:
            return "A"
        elif 3.5 <= self.score < 4.0:
            return "B+"
        elif 3.0 <= self.score < 3.5:
            return "B"
        elif 2.5 <= self.score < 3.0:
            return "C+"
        elif 2.0 <= self.score < 2.5:
            return "C"
        else:
            return "F"

    def print_student_info(self):
        print(f'{self.sno}\t{self.name}\t{self.major}\t{self.score}()')

student = Student()
student.setting_data('20211111', '홍길동', '컴퓨터공학과', 3.45)
student.print_student_info()










