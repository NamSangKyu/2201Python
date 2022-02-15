#다중 반환
# , --> 데이터 및 변수를 구분
def return_multi(*args):
    return sum(args),sum(args)/len(args),max(args),min(args)

# 리턴 값 개수에 맞추어서 받음
s, a, m, n = return_multi(1,2,3,4,5,6,7,8,9,10)
# 변수가 하나면 튜플로 만들어서 받음
d = return_multi(1,2,3,4,5,6,7,8,9,10)
print(s,a,m,n)
print(d)
