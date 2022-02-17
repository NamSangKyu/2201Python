import random as r

#사용자로부터 로또번호 6개를 입력받음
#단, 중복된 숫자 X
lotto_set = set()
while len(lotto_set) < 6:
    n = int(input("로또번호를 입력 하세요 >>> "))
    if n < 1 or n > 45:
        print("로또번호는 1~45 사이로 입력하세요")
        continue
    lotto_set.add(n)
print('입력한 로또번호 목록 : {}'.format(lotto_set))
