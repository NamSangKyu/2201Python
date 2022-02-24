import time

file = open(time.strftime('%Y-%m-%d')+'.txt','at',encoding="UTF-8")
while True:
    schedule = input('오늘의 스케줄을 입력하세요 >>>')
    if not schedule:
        break
    file.write(schedule + '\n')
file.close()