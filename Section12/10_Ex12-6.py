from datetime import *

#작업 전 현재 날짜 시간 뽑음
start = datetime.now()
total = 0
for num in range(1,10000001):
    total += num
#작업 후 현재 날짜 시간을 뽑음
end = datetime.now()

elapse = end - start
elapse = elapse.total_seconds()

print('총합은 {} 입니다.'.format(total))
print('총 {}초가 소요되었습니다.'.format(elapse))