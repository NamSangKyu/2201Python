#메모리 주소 안바뀌는 형태
#mutable --> list, set, dict
lst = [1,2,3,4,5]
print(id(lst))
lst.append(6)
print(id(lst))
lst.pop(0)
print(id(lst))
s = {1,3,4,5}
print(id(s))
s.pop()
print(id(s))
s.add(100)
print(id(s))
#메모리 주소가 바뀌는 형태
#immutable --> int, float, str, tuple
num = 10
print(num,id(num))
num = 20
print(num,id(num))
num = 10
print(num,id(num))
num += 20
print(num,id(num))
newNum = num #동일한 메모리 주소를 저장되는 경우
print(id(num), id(newNum))






