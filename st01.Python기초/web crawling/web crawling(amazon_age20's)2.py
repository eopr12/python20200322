# 페이지의 elements 모두 가져오기
html = driver.page_source

# Beautiful Soup로 웹페이지 전체출력하기
soup = BeautifulSoup(html, 'html.parser')

print(soup)

# Beautiful Soup로 메타 데이터만 찾아서 content 속성값 가져오기
for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))

# Beautiful Soup로 원하는 태그 내용 가져오기
print (bsObject.head.find("meta", {"name":"description"}).get('content'))