## 네이버 로그인 하기 ##

from selenium import webdriver
from bs4 import BeautifulSoup

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login')

# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('eopr12')
driver.find_element_by_name('pw').send_keys('qlqjs31690@@')

# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# 네이버페이 주문내역 페이지 접속

driver.get('https://order.pay.naver.com/home')

# 페이지의 elements 모두 가져오기
html = driver.page_source

# Beautiful Soup 사용하기
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.p_inr > div.p_info > a > span')

for n in notices:
    print(n.text.strip())


##1.원래는 urlopen을 수행할때 검색어가 포함되어 있어서 beautifulsoup로 바로 가져오면 됐지만, 이제는 페이지를 다 로딩한 후 검색어를 동적으로 불러오니 위의 코드로 가져오는 것은 불가능합니다.
##따라서 이제는 브라우저를 모방하는 selenium 등을 추가로 사용해야함
##2.로그인 보안문자에서 막히는데 네이버 정책 업데이트되서 selenium도 막힌건지
##3.아마존은 url 끝에 /robots.txt 입력해도 크롤링 허가/비허가 사항이 안나오는데 국내사이트만 나타나는건지