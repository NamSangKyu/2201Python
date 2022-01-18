name='홍길동'
age = 20

# format 함수
msg1 = '이름 : {}\t\t나이 : {}'.format(name,age)
msg2 = '이름 : {0}\t\t나이 : {1}'.format(name,age)
msg3 = '이름 : {1}\t\t나이 : {0}'.format(name,age)
print(msg1)
print(msg2)
print(msg3)

# 3.6 버전 이상
msg4 = f'이름 : {name}\t\t나이 : {age}'
print(msg4)





