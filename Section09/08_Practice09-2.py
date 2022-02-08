lst = []
while True:
    score = int(input('점수 입력 >>> '))
    if score < 0:
        break
    lst.append(score)

print(f'평균={sum(lst) / len(lst)}, 최대값={max(lst)}, 최소값={min(lst)}')