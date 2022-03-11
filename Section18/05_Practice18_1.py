import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'

response = requests.get(url)
html = response.text
#print(html)
soup = BeautifulSoup(html,'html.parser')
#클래스속성 비교 class_='title'
movie_in_list = soup.find_all('td',class_='title')
for movie in movie_in_list:
    print(movie.find('a').text)







