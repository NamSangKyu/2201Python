#가변 매개변수, 받아온 데이터를 튜플로 관리
def printItems(*args):
    print(args)
    for item in args:
        print(item, end=" ")
    print()
printItems('Hello', 'Python', 'Wellcome','Test')
printItems('홍길동')

#매개변수에 기본값을 설정하는 디폴트 매개변수
def printMessage(msg='안녕하세요'):
    print(msg)

printMessage()
printMessage('만나서 반갑습니다.')

#매개변수에 디폴트 값을 설정할때는
#반드시 오른쪽 끝에서부터 설정
def printNumbers(n1,n2=10):
    print(n1,n2)
printNumbers(20)


