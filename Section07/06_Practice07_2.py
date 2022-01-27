no = int(input('임의의 양수를 입력하세요 >>> '))
total = 0

for i in range(1, no + 1):
    total += i

print('1부터 {}사이 모든 정수의 합계는 {}입니다.'.format(no,total))