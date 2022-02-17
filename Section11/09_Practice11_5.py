"""
    숫자 1~100까지 숫자들 중 완전수만 출력
    완전수 :자기자신의 약수를 제외한 약수들의 합이 자기 자신인 숫자
           6의 약수 : 1, 2, 3 ,6
                   1 + 2 + 3 == 6
"""
def check_perfect_number(n):
    lst = []#약수만 저장되는 리스트
    for i in range(1,n):
        if n % i == 0:
            lst.append(i)
    return sum(lst) == n

for n in range(1,101):
    if check_perfect_number(n):
       print(n,end=" ")

