"""
    함수 (Function)
        자주 사용하는 기능을 내장함수 처럼 미리 만들어 놓은 코드
        필요할 때마다 불러서 쓴다.

    함수 문법
    def 함수명([매개변수....]):
        실행할 코드
        [return 반환값]
"""
#인수 X, 반환값 X
def printWelcome():
    print('Hello Python')
    print('Nice to meet you')

printWelcome()

#인수 X, 반환값 O
def inputNumber():
    no = int(input("숫자 하나 입력하세요 >>> "))
    return no

print(inputNumber() * 2)

#인수 O, 반환값 X
def printPersonInfo(name,age):
    print(f'{name}님의 나이가 {age}살 입니다.')

printPersonInfo("홍길동",20)
#매개변수 개수만큼 데이터를 안보내면 에러
#printPersonInfo("홍길동")





