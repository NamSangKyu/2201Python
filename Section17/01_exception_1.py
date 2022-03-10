n1 = int(input('숫자 입력 >>> '))
n2 = int(input('숫자 입력 >>> '))
try: #작업할 코드 영역
    print(n1/n2)
except: #try에서 코드 실행 중 에러가 발생 했을때 에러를 처리하는 영역
    print('0으로 나눌 수 없습니다.')

print('프로그램 종료')