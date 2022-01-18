#input() 함수
#input('화면에 출력할 내용')
#문자열로 입력 받은후 원하는 타입으로
#형변환하는 작업이 필요함
name = input('이름을 입력하세요 : ')
print('입력하신 이름은 {}'.format(name))

print(type(name))

# 정수 입력 - int
num = int(input("숫자 하나 입력 : "))
print(num,type(num))

# 실수 입력 - float
r = float(input("원의 반지름 하나 입력 : "))
print(r, type(r))







