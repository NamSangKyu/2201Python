import random as r
import time as t
import math as m

#정수 생성
answer = r.randrange(1,101)
start = t.time()
while True:
    n = int(input('어떤 값일까요? >>> '))
    if n == answer:
        print("정답입니다.")
        break
    elif n > answer:
        print("Down")
    else:
        print("Up")
end = t.time()
total = m.ceil(end - start)
print(f'{total}초만에 성공 했습니다.')






