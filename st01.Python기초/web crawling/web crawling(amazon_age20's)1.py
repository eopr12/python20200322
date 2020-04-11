## 네이버 로그인 하기 ##

from urllib.request import urlopen
from bs4 import BeautifulSoup

# url에 접근한다.
html = urlopen("https://www.amazon.com")
bsObject = BeautifulSoup(html, "html.parser")

# Beautiful Soup로 모든 링크와 텍스트와 주소 가져오기
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))


#strip() == 데이터 양옆 공백제거
#get_text() == 데이터에서 문자열만 추출
