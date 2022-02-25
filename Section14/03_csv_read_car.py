"""
car.csv 파일을 읽은 후 파일에서 4번째 데이터가 판매금액
사용자로부터 입력 받은 금액 이상인 데이터만 출력
"""
money = int(input('금액을 입력 하세요 >>> '))

with open('car.csv','rt') as file:
    while True:
        line = file.readline()
        if not line:
            break
        line = line.replace('\n','')
        arr = line.split(',')
        if money <= int(arr[3]):
            print("{:20s} {:15s} {:4s} {:4s}".format(arr[0],arr[1],arr[2],arr[3]))