#유니코드에 해당하는 글자를 뽑는 함수
print(chr(65))  #A
print(chr(66))  #B
print(chr(67))  #C
print(chr(68))  #D
print(chr(90))  #Z
print(chr(97))  #a
print(chr(122)) #z
#----------------------------
#알파벳 대문자 소문자 A~Z
for i in range(65,91):
    print(chr(i),"-",chr(i+32))
#------------------------------
print(ord('A'), ord('a'))#문자 -> 유니코드
print(ord('가'), ord('나'))#문자 -> 유니코드
#------------------------------
#eval : 연산식을 넣으면 해당 연산식을 계산해서
#       결과값을 리턴하는 함수
print(eval("100+200"))
a = 10
print(eval("a*5"))
print(eval("min(10,20,30,40)"))
#-------------------------------
print(format(1000000)) #str(1000000)
print(format(1000000,","))
print(format(1000000,"_"))
#-------------------------------
print(str(100) + "Hello")










