no = int(input("정수를 입력하세요 >>> "))

if no > 0:
    i = 1
    while i<=no:
        print(f'{i}번째 Hello')
        i+=1
else:
    print('잘못된 입력입니다.')