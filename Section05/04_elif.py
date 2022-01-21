age = int(input("몇살 입니까 >>> "))

if age >= 20:
    print('성인')
elif age >= 17:
    print('고등학생')
elif age >= 14:
    print('중학생')
elif age >= 8:
    print('초등학생')
else:
    print('미취학')
