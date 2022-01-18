"""
    딕셔너리(dict)
        데이터1 - 데이터2 한쌍으로 저장
        Key      Value
        키값과 저장할 값이 한쌍으로 저장
        키값을 이용해서 데이터를 읽기, 저장, 삭제, 수정

        키값은 중복이 안됨, 저장할 값은 중복이 됨
"""
#딕셔너리 생성   Key : Value
dict1 = {'홍길동':20,'김철수':44,'이영희':35}
print(dict1)
#딕셔너리변수[키값] ---> 키값에 해당하는 값을 읽어옴
#키값이 홍길동에 해당하는 값을 읽어옴
print(dict1['홍길동'])
print(dict1['김철수'])
#중간에 에러가 발생하면 프로그램이 바로 종료
#print(dict1['김영희']) #키값이 없을경우?
#딕셔너리 생성
dict2 = dict(A = 'TEST', B = False)
print(dict2['A'])
print(dict2['B'])
#데이터 추가
dict1['김영희'] = 99
dict1['김철수'] = 99 #김철수에 해당하는 값을 변경
print(dict1)
dict2.setdefault('C','Hello')
print(dict2)
#삭제
dict1.pop('김철수')
#dict1.pop('김철수')#삭제할 키값이 없으면 에러 발생
print(dict1)
dict1.popitem()#맨 마지막 키값에 해당하는 데이터 삭제
print(dict1)
#수정
dict2['A'] = 24 #수정할 키값이 없으면 새로 데이터 추가
print(dict2)




