import csv

with open('차량관리.csv','wt',newline='',encoding='utf-8') as file:
    csv_maker = csv.writer(file,delimiter=',',quotechar='"')
    csv_maker.writerow([1,'08러1234','2020-10-20 14:00'])
    csv_maker.writerow([2,'25다1234','2020-10-20 14:10'])
    csv_maker.writerow([3,'28가1234','2020-10-20 14:20'])
    csv_maker.writerow([4,'32호1234','2020-10-20 14:30'])
print("csv 파일이 생성되었습니다.")

with open('차량관리.csv','rt',encoding='utf-8',newline='') as file:
    csv_reader = csv.reader(file,delimiter=',',quotechar='"')
    for line in csv_reader:
        print(line)






