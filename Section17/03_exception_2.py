
try:
    n1 = int(input('숫자 입력 >>> '))
    n2 = int(input('숫자 입력 >>> '))
    print(n1/n2)
except ValueError: #ValueError만 처리
    print('숫자가 아닌 다른 문자열을 입력했습니다.')
except ZeroDivisionError: #0으로 나눈 에러만 처리
    print('0으로 나눌수 없습니다.')
print('프로그램 종료')
