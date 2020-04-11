from selenium import webdriver

# Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
driver = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")

# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://google.com')
