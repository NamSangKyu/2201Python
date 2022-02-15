"""
    전역 변수 : 함수 위치에 상관없이 어떤 함수에서도
               동일하게 접근이 가능한 변수
    지역 변수 : 특정 영역에서만 접근이 가능한 변수
               함수 및 실행 영역이 끝나면 바로 메모리에서 해제됨
"""
age = 100 #전역변수 - 함수 밖에 선언된 변수
def printA():
    print("printA :",age)

def printB():
    print("printB :",age)
printA()
printB()

#printC함수가 끝나면 지역변수인 msg는 메모리에서 해제
def printC():
    msg = 'Hello Python' #지역변수로 선언
    print('printC',msg)
printC()
#msg가 printC에서만 존재하기 때문에 외부에서는 msg 존재를 모름
#print(msg)

