#절대값 구하는 함수
print(abs(10), abs(-10))
#몫과 나머지를 구하는 함수 - 결과는 튜플
print(divmod(10,7)) #몫 - 1, 나머지 - 3
#문자열을 정수로 바꾸는 함수
print(int('100')*2)
#문자열을 실수로 바꾸는 함수
print(float('3.1415')*2)

lst = [123,15,2,15,56,21,6,100]
#최대값 구하는 함수
print(max(lst),max(12,5,3,1,67,112,54))
#최소값 구하는 함수
print(min(lst),min(12,5,3,1,67,112,54))
#거듭제곱
print(pow(2,2)) #2의 2승 - 4
print(pow(2,-2)) #2의 -2승 - 0.25
print(pow(2,10)) #2의 10승 - 1024

#반올림
print(round(156.123456,0))
print(round(156.123456,1))
print(round(156.123456,2))
print(round(156.123456,4))
print(round(156.123456,-1))
print(round(156.123456,-2))
#총합 함수
list1 = [12,4,53,42,12,11,4,5,34,3]
list2 = ['H','e','l','l','o']
print(sum(list1))
#숫자 이외의 값은 sum 함수를 사용할수 없음, 에러처리
#print(sum(list2))








