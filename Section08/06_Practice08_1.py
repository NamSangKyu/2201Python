#금액 10000원 설정
money = 10000
print(f'현재 {money}원 있습니다.')
#반복문
while True:
    #사용할 금액 입력 받음
    m = int(input("사용할 금액 입력 >>> "))
    #사용할 금액이 0보다 작거나 같은지 체크
    if m <= 0:
        print("0 이하의 값은 입력할 수 없습니다.")
        #조건이 True면 다시 입력
        continue
    #조건이 거짓이면 사용할 금액에서 차감
    #차감 후 금액이 음수면 차감을 하지 않음
    if money - m < 0:
        print(f'{m - money}원이 부족합니다.')
        continue
    #차감 후 금액 0이면 반복문을 종료
    money -= m
    print(f'현재 {money}원 있습니다.')
    if money == 0:
        break

