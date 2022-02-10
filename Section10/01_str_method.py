#정렬
print('오른쪽 정렬 : {:>10d}'.format(123))
print('오른쪽 정렬 : {:>10s}'.format('A'))
print('왼쪽 정렬 : {:<10d}'.format(123))
print('왼쪽 정렬 : {:<10s}'.format('A'))
print('가운데 정렬 : {:^10d}'.format(123))
print('가운데 정렬 : {:^10s}'.format('A'))

# 빈공간을 *로 채움(빈공간을 채우는 문자 하나만 허용)
print('왼쪽 정렬 : {:*<10d}'.format(123))
print('오른쪽 정렬 : {:*>10d}'.format(123))
print('가운데 정렬 : {:*^10d}'.format(123))

print('----------------------------------------')
#    012345678901234567
s = 'Hello World Test World In Python'
print(s.count('World')) # World의 개수
print(s.count('World',11)) # 인덱스가 11부터 World의 개수
print('----------------------------------------')
print(s.find('World')) #처음부터 World가 위치를 찾음
print(s.find('World',11))#11번 인덱스부터 World가 위치를 찾음
print(s.rfind('World')) #끝에서부터 World가 위치를 찾음
print(s.find('Java')) #찾는 문자열이 없으면 -1 리턴
print('----------------------------------------')
print(s.index('World'))
#print(s.index('Java')) #찾는 문자열이 없으면 에러를 발생
print('----------------------------------------')
print(s.upper()) #전부 대문자로 변경
print(s.lower()) #전부 소문자로 변경
print(s.capitalize())#첫글자만 대문자, 나머지 소문자로 변경
print('----------------------------------------')
lst = ['A','B','C','D','E']
print('+'.join(lst))#+로 리스트의 각 요소들을 하나의 문자열로 합쳐줌
l = '+'.join(lst)
print(l.split('+')) # +로 문자열을 쪼개서 리스트로 생성
print('----------------------------------------')
print(s.replace('World','Hell')) #World를 전부 Hell로 바꿈
s1 = '                     A'
s2 = 'A                     '
s3 = '          A           '
print(s1.lstrip(), len(s1.lstrip())) #왼쪽에 있는 공백을 전부 제거
print(s2.rstrip(), len(s2.rstrip())) #오른쪽에 있는 공백을 전부 제거
print(s3.strip(), len(s3.strip())) #양쪽에 있는 공백을 전부 제거

s1 = '..............A'
print(s1.lstrip('.'), len(s1.lstrip('.'))) #왼쪽에 있는 . 을 전부 제거








