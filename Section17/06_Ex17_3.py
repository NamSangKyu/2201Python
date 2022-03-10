try:
    score = int(input('점수를 입력하세요 >>> '))
    if score < 0 or score > 100:
        # Exception 강제 발생 - Exception 종류에 해당하는 객체를 생성
        raise Exception('점수는 0~100사이 입니다.')
    if score >= 80:
        print('{}점 합격입니다.'.format(score))
    else:
        print('{}점 불합격입니다.'.format(score))
except Exception as e:
    print(e)

