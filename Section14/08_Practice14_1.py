fileName = ''
while True:
    fileName = input('복사할 파일명을 입력하세요 >>> ')
    f = fileName.split(".")
    if f[-1] == "txt":
        break
    print('복사할수 없는 파일 입니다.')

with open(fileName,'rt',encoding='utf-8') as file:
    with open('복사본-'+fileName,'wt',encoding='utf-8') as fwrite:
        str = file.read()
        fwrite.write(str)
print('복사본-'+fileName+' 파일이 생성되었습니다.')
