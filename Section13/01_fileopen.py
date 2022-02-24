"""
    파일 모드
        읽기 - r, 쓰기 - w, 추가 - a, 베타적 추가 - x
    파일 종류
        텍스트 파일 - t,  이진 파일 - b

    wt ===> 쓰기전용 텍스트 파일
    rt ===> 읽기전용 텍스트 파일
"""
#파일 열기
#파일을 쓰기모드 열었음, 쓰기모드로 열면 파일을 매번 새로 생성
#파일을 생성할때는 폴더가 미리 만들어져 있어야 함, 폴더는 자동생성 X
file = open('c:/test/firstFile.txt','wt',encoding="UTF-8")
print('파일 오픈 완료')
print(file)
file.close()#파일 닫기

with open('secondFile.txt','wt',encoding="UTF-8") as file:
    print('파일 오픈 완료')
    print(file)
    #with 영역이 끝나면 자동으로 파일이 close 처리








