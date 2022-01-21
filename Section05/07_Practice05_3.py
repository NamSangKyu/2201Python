num1 = int(input("정수1 입력 >>> "))
num2 = int(input("정수2 입력 >>> "))
num3 = int(input("정수3 입력 >>> "))

result = 0
# result = num1 if num1 > num2 else num2
# result = result if result > num3 else num3

if num1 > num2:
    result = num1
else:
    result = num2

if result < num3:
    result = num3
print(f'가장 큰 수는 {result}입니다.')