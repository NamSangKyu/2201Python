employee_no = int(input("4자리 사원번호를 입력하세요 >>> "))
msg = '오전' if employee_no % 10 >= 5 else '오후'
print(f'근무 시간은 {msg}입니다.')