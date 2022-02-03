'''
    숫자 하나를 입력 받아서
    입력한 숫자의 약수를 전부 출력
    break문을 사용은 선택
    숫자입력 >> 10
    약수 목록 : [1, 2, 5, 10]
'''
num = int(input("숫자 하나 입력 >>> "))
lst = []
for i in range(1,num//2+1):
    if num % i == 0:
        lst.append(i)
lst.append(num)
print(f'약수 목록 : {lst}')

