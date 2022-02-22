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

#로또 당첨번호 랜덤하게 뽑음 1~45까지 숫자, 7개를 뽑음
#마지막 번호는 보너스 번호로 취급
winning_lotto_numbers = r.sample(range(1,46),7)
print('당첨된 로또번호 목록 : {}'.format(winning_lotto_numbers))

#당첨 등수 및 낙첨 정보 출력
count = 0 #일치하는 번호 개수
for i in range(len(winning_lotto_numbers)-1):
    if winning_lotto_numbers[i] in lotto_set:
        count += 1

if count == 6:
    print("1등에 당첨 되셨습니다.");
elif count == 5 and winning_lotto_numbers[-1] in lotto_set:
    print("2등에 당첨 되셨습니다.");
elif count == 5:
    print("3등에 당첨 되셨습니다.");
elif count == 4:
    print("4등에 당첨 되셨습니다.");
elif count == 3:
    print("5등에 당첨 되셨습니다.");
else:
    print("낙첨 되셨습니다.");
    







