lst = []
for i in range(1, 100):
    msg = ''
    if i // 10 > 0 and (i // 10 % 3 == 0 or i // 10 % 6 == 0 or i // 10 % 9 == 0):
        msg = '짝'
    if i % 10 != 0 and (i % 10 % 3 == 0 or i % 10 % 6 == 0 or i % 10 % 9 == 0):
        msg += '짝'
    if msg == '':
        lst.append(i)
    else:
        lst.append(msg)
count = 1
for i in range(len(lst)):
    print(lst[i],end='\t\t')
    if count % 10 == 0:
        print()
    count += 1
