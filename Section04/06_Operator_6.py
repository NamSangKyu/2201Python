#시퀸스 연산자
#리스트, 튜플, 문자열 등에서 서로 연결할때 사용하는 연산자
lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2 #리스트 두개를 합치는 연산
print(lst3)
str1 = 'Hello'
str2 = 'World'
print(str1 + str2)
#in, not in
print(10 in lst3) #lst3에 10이 있냐?
print(2 in lst3)  #lst3에 2가 있냐?
print(10 not in lst3) #lst3에 10이 없냐?
print(2 not in lst3)  #lst3에 2가 없냐?
print('e' in str1) #str1 문자열에 e 가 있냐?
print('e' not in str1)#str1 문자열에 e 가 없냐?
#삼항 연산자
#조건식의 결과에 따라서 True 일때 나타낼 식, False 일때 나타낼 식을 표현
n = 9
#           참        조건식          거짓
message = "짝수" if n % 2 == 0 else "홀수"
print(message)
#반복 연산
print("A" * 3)
print("A" * 4)
print("A" * 5)






