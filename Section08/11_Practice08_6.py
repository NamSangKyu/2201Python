'''
숫자 두개를 입력 받아서
두숫자의 최대공약수를 출력

공약수 : 두숫자를 공통적으로 나누었을때
        나누어서 떨어지는 경우

첫번째 숫자 입력 >>> 5
두번째 숫자 입력 >>> 10
두수의 최대 공약수 : 5
'''

n1 = int(input('첫번째 숫자 입력 >>> '))
n2 = int(input('두번째 숫자 입력 >>> '))
gcm = 1

if n1 > n2:
    temp = n1
    n1 = n2
    n2 = temp

for i in range(2, n1+1):
    if n1 % i == 0 and n2 % i == 0:
        gcm = i

print(f'두수의 최대 공약수 : {gcm}')











