i = 1

while i < 10:
    dan = 2
    while dan < 10:
        print(f'{dan} * {i} = {dan*i}',end="\t")
        dan += 1
    print() #아무 내용이 없으면 줄바꿈만 수행
    i+=1