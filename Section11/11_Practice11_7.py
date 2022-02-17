"""
    매개변수로 문자열 하나를 받아서
    해당 문자열이 회문인지 체크하는 함수
    회문이면 True 리턴, 회문이 아니면 False 리턴

    회문 >>> lol , 스위스

     0   1   2   3   4      0   1  2
     H   e   l   l   o      스  위 스
    -5  -4  -3  -2  -1      -3 -2 -1
"""
def check_palindrome_1(str):
    for i in range(len(str)//2):
        if str[i] != str[-(i+1)]:
            return str + "는 회문이 아닙니다."
    return str + "는 회문 입니다."

def check_palindrome_2(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]:
            return str + "는 회문이 아닙니다."
    return str + "는 회문 입니다."
str = input("문자열 입력 >>> ")
print(check_palindrome_1(str))
print(check_palindrome_2(str))











