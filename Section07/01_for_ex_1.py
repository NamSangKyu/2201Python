lst = [1,2,3,4,5]
for n in lst: #리스트에 저장된 데이터를 하나씩 꺼내서 n에 저장해서 반복
    print(n, end="\t")
print('\n---------------------')
s = {1,1,3,2,5}
for n in s: #셋에 저장된 데이터를 하나씩 꺼내서 반복
    print(n, end="\t")
print('\n---------------------')
str = "Hello World"
for n in str: #문자열은 한글자씩 꺼내서 반복
    print(n, end="\t")
print('\n---------------------')
dic = {'A' : 1, 'B' : 2, 'C' : 3}
for n in dic: #딕셔너리 경우에는 키값만 하나씩 꺼내서 반복
    print(f'{n} - {dic[n]}', end="\t")
print('\n---------------------')
tu = (1,2,3,4,5)
for n in tu: #튜플에 저장된 데이터를 하나씩 꺼내서 반복
    print(n, end="\t")
print('\n---------------------')





