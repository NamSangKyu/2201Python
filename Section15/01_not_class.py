'''
    사람 인적 정보를 저장하는 변수
    이름, 나이

    인적 정보를 출력 --> 함수 작성

    각각의 변수들과 함수가 분리가 되어있기 때문에
    관리 및 처리가 불편하다 ---> 함수와 메서드를 모아서 하나의 형태로 작성 --> 클래스
'''
def print_person(name, age):
    print(name," ",age)

name = '홍길동'
age = 20

print_person(name,age)