#반복문 이용하여 구구단 2단~9단 출력
dan = 2
while dan < 10:
    i = 1
    while i < 10:
        print(f'{dan} * {i} = {i * dan}')
        i += 1
    dan += 1