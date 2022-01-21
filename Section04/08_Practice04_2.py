seconde = int(input('초를 입력하세요 >>> '))
hour = seconde // 3600
seconde %= 3600
minute = seconde // 60
seconde %= 60
print(f'변환 결과는 {hour}시간 {minute}분 {seconde}초입니다.')
