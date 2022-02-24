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
file = open('firstFile.txt','wt',encoding="UTF-8")
print('파일 오픈 완료')
print(file)
file.close()#파일 닫기

