'''
    리스트(List)
        데이터를 원하는 만큼 여러개 데이터를 저장
        1. 중복된 데이터가 저장
        2. 데이터를 추가한 순서가 보장
        3. 추가, 삭제, 수정이 가능
'''
#리스트 생성
#        0 1  2      3 4  5    6
list1 = [1,2,'Hello',4,5,True,'World']
#       -7 -6  -5   -4-3 -2     -1
print(list1)
#리스트도 인덱스 번호를 이용해서 하나씩 데이터를 뽑을수가 있음
print(list1[0])
print(list1[2])
print(list1[5])
print(list1[-1])
print(list1[-5])
#print(list1[7])
print('-----------------')
#리스트 1번 인덱스부터 4번 인덱스까지 추출
print(list1[1:5])
#추출한 리스트를 새 리스트로 생성
#기존 리스트 내용은 그대로 유지됨
list2 = list1[1:5]
print(list1,list2)
#리스트1의 마지막 데이터 2개 추출
print(list1[-2:])

#추가, 삭제, 수정
#리스트에 데이터 추가, 맨뒤에 추가
list1.append("Test")
list1.append(100)
print(list1)
#3번 인덱스에 데이터를 끼워 넣기, 한칸씩 뒤로 밀림
list1.insert(3,111)
print(list1)
#수정
list1[3] = 'Hello'
print(list1)
#리스트 6번 인덱스 값을 'Hello'로 수정
list1[6] = 'Hello'
print(list1)
#삭제
#pop은 인덱스 번호에 해당하는 데이터를 삭제
#인덱스 번호를 안쓰면 마지막 데이터를 삭제
list1.pop()
print(list1)
# 1번 인덱스에 해당하는 데이터를 삭제
list1.pop(1)
print(list1)
#리스트 데이터 삭제시 데이터를 검색해서 삭제
list1.remove('Test')
print(list1)
# Hello 데이터 삭제
list1.remove('Hello') #최초 검색된 1개 데이터를 삭제
print(list1)
#World 데이터가 있는 인덱스 번호
print(list1.index('World'))
#print(list1.index('Test')) #데이터가 없으면 에러

#전체 데이터 삭제
list1.clear()
print(len(list1))







