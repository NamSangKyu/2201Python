#목록 한건당 인덱스와 값을 튜플로 꺼냄
lst = ['서울','대전','대구','부산']
for item in enumerate(lst):
    print(item)
#목록 한건당 인덱스와 값을 따로 꺼냄
for index, item in enumerate(lst):
    print(index, item)
#---------------------------------
print(list(range(10))) #0~9  0~(마지막값 - 1)
print(list(range(0, 10))) #0~9 시작값,(마지막값 - 1)
print(list(range(0, 10, 2))) #시작값,(마지막값 - 1),증감값
#---------------------------------
#len ---> 저장되어 있는 데이터 개수를 구하는 함수
print(len(lst))
print(len(range(5)))
print(len([1,2,54,2,1,5,3,2]))
#정렬
list1 = [5,23,1,6,2,6,8,9,3,5]
print(sorted(list1))
print(sorted(list1,reverse=True))
print(sorted(list1,reverse=False))
list2 = ['F','G','Z','A','B','E']
print(sorted(list2))
#zip - 각 리스트별 한개씩 튜플로 합쳐서 리턴 
list1 = [41,52,67,43,22]
list2 = ['F','G','Z','A','E']
for item in zip(list1,list2):
    print(item)









