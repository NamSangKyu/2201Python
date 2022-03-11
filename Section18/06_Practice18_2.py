import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'

response = requests.get(url)
html = response.text
#print(html)
soup = BeautifulSoup(html,'html.parser')
#클래스속성 비교 class_='title'
movie_in_list = soup.find_all('td',class_='title')
count = 0
for movie in movie_in_list:
    count += 1
    print(count,"위 :",movie.find('a').text)







