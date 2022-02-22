import datetime as dt

print(dt.datetime.now())

birthday = dt.date(2020,11,5)
print(birthday)

wake = dt.time(20,21,33)
print(wake)

date = dt.datetime.now()
print(date.year)
print(date.month)
#date.day = 15 #수정 X
print(date.day)
print(date.hour)
print(date.minute)
print(date.second)
print(date.microsecond)

date = date.replace(2021,12,31,0,0,0,0)
print(date)

today = dt.datetime.now()
tomorrow = today + dt.timedelta(days=1)
print(tomorrow)

#다음주 화요일 날짜 계산
next_week = today + dt.timedelta(weeks=1)
print(next_week)

date1 = dt.date(2022,2,22)
date2 = dt.date(2022,2,23)
print(date2-date1)
print((date2-date1).total_seconds()/(24 * 60 * 60))

#오늘 날짜를 기준으로 수능까지의 D-day 출력
date2 = dt.date(2022,11,17)
print((date2-date1).total_seconds()/(24 * 60 * 60))
#오늘 날짜를 기준으로 연말까지의 D-day 출력
date2 = dt.date(2022,12,31)
print((date2-date1).total_seconds()/(24 * 60 * 60))












