count = 5

while count > 0:
    #비밀번호 입력
    passwd = input('비밀번호를 입력하세요 >>> ')
    #비밀번호 qwerty 인지 체크
    if passwd == 'qwerty':
        #'비밀번호를 맞췄습니다.' 출력 멈춤
        print('비밀번호를 맞췄습니다.')
        break
    else:
        #틀리면 횟수 -1
        count -= 1
#횟수를 전부 소진하면 '비밀번호 입력횟수를 초과했습니다'
if count == 0:
    print('비밀번호 입력 횟수를 초과했습니다.')