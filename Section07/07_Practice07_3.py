# lst = []
#
# no = int(input("몇 개의 과일을 보관 할까요? >>> "))
# for i in range(1, no+1):
#     lst.append(input('{}번째 과일을 입력하세요 >>> '.format(i)))
#
# print('입력받은 과일들은 {}입니다.'.format(lst))

lst = []

no = int(input("몇 개의 과일을 보관 할까요? >>> "))

while no != len(lst):
    lst.append(input('{}번째 과일을 입력하세요 >>> '.format(len(lst)+1)))
print('입력받은 과일들은 {}입니다.'.format(lst))







