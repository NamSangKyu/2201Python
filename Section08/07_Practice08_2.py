while True:
    #영화 평점을 입력
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    #평점 1~5 사이 인지 체크
    if 1 <= score <= 5:
        #True면 평점을 ★ 개수로 출력
        print(f'평점 : {"★"*score}')
        break
    else:
        #False면 메세지 출력
        print("평점은 1~5 사이만 입력할 수 있습니다.")