score = int(input("국어 점수를 입력하세요 >>> "))
score += int(input("영어 점수를 입력하세요 >>> "))
score += int(input("수학 점수를 입력하세요 >>> "))
score /= 3 #평균
msg = '합격' if score >= 80 else '불합격'
print(f'평균은 {score}이고 결과는 {msg}입니다.')