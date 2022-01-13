'''
    튜플(tuple)
        데이터를 리스트 처럼 저장
        데이터를 읽는 방식도 리스트와 동일
        단, 최초에 저장한 데이터만 유지
        튜플에서는 데이터를 추가 삭제 수정 X
'''
#튜플 생성
tup1 = (1, 41,'Hello', False, 'Test', True)
print(tup1)
tup2 = 1, 41, 'Hello', False, 'Test', True
print(tup2)
lst = [1, 'Test', True, 100]
tup3 = tuple(lst)
print(tup3)
tup4 = tuple(lst[:2])
print(tup4)
#tup1[0] = 111 #수정 X
print(tup1[0],tup1[1]) #리스트와 동일하게 조회는 가능
# 튜플을 리스트로 저장
list1 = list(tup1)
print(list1)
# 리스트 처럼 부분 추출 가능
print(tup1[:2])







