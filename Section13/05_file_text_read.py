#파일 열기 - 읽기모드에서는 파일이 있어야됨, 없으면 에러발생
file = open('text.txt','rt',encoding='UTF-8')
#파일 내용 읽어오기
str = file.read() #전체 내용 읽기
print(str)
#파일 닫기
file.close()

print("-----------------------")
file = open('text.txt','rt',encoding='UTF-8')
while True:
    str = file.read(5)#5글자씩 읽음
    if not str:
        break
    print(str,end="")
file.close()
print("-----------------------")
file = open('text.txt','rt',encoding='UTF-8')
while True:
    str = file.readline()
    if not str:
        break
    print(str,end="")
file.close()
print("-----------------------")
file = open('text.txt','rt',encoding='UTF-8')
#파일 내용을 한줄씩 읽어와서 리스트로 생성
line_list = file.readlines()
print(line_list)
for line in line_list:
    print(line,end="")
file.close()








