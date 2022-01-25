car_no = input("차량번호를 입력하세요 >>> ")
if int(car_no[-1]) % 2 == 0:
    print(f'차량번호 \'{car_no}\'는 오늘 운행가능입니다.')
else:
    print(f'차량번호 \'{car_no}\'는 오늘 운행불가능입니다.')

