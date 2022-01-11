'''
    변수(variable)
        데이터를 하나 저장할 공간

    주석 단축키 : Ctrl + /
'''
#box라는 이름으로 공간을 하나 만들고
#데이터는 숫자 10을 저장
box = 10
# 변수 옆에 = 이 없으면 계산하는 용도로 쓰임
# 변수가 저장하고 있는 값을 읽어옴
print(box)
box = 20
box = 30
print(box)
t = 200
print(t)
print(box + t)
#t와 box 뺀 결과를 result에 저장
result = t - box
print(result)
#box의 값을 바꿔도 result는 변함 없음
box = 100
print(result)
# 다시 계산해서 저장해야 데이터가 갱신
result = t - box
print(result)










