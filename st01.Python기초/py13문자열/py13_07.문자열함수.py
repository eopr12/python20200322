
#################################
# 중요 문자열 함수 / 문자열 메서드
#################################
# len()	길이를 구하는 함수
# sorted()	오름차순 정렬
# reversed()	내림차순 정렬
# .format()	포매팅 함수
# .upper()	대문자로 변환 함수
# .lower()	소문자로 변환 함수
# .strip()	양쪽 줄바꿈문자나 공백 문자 제거 함수
# .lstrip()	왼쪽 줄바꿈문자나 공백 문자 제거 함수
# .rstrip()	오른쪽의 줄바꿈문자나 공백 문자 제거 함수
# .count()	문자열에서 문자나 문자열의 개수 세기
# .index()	문자열에서 왼쪽부터 첫번째 위치 찾기 함수
# .find()	문자열에서 왼쪽부터 첫번째 위치 찾기 함수
# .rfind()	문자열에서 오른쪽부터 첫번째 위치 찾기 함수
# .split()	문자열을 문자로 자르기 함수
# .join()	문자열 삽입(join)

# 문자열 길이(len)
a = "hobby"
length = len(a)  # 5
print(length)

# 문자열 개수 세기(count)
a = "hobby"
length = a.count("b")  # 5
print(length)

# 위치 알려주기1(find) ==>문자열은 find함수 쓰기
a = "python is best choice"
pos = a.find("b")  # 10
print(pos)
pos = a.find("k")  # -1 ==>없다
print(pos)

# 위치 알려주기2(index)
# index 를 사용할 때는 try except 로 감싸야 한다
a = "python is best choice"
pos = a.index("b")  # 10
pos = a.index("k")  # ==>Value Error발생,try except로 감싸야 다음 코드 결과값 나옴

# 문자열 삽입(join)
a = ","
jo = a.join("abcd")  # "a,b,c,d"
print(jo)

# 소문자를 대문자로 바꾸기(upper)

# 대문자를 소문자로 바꾸기(lower)

# 양쪽 공백 지우기(strip)
a = "   hi   "
a = a.strip()
print(a)

# 문자열 바꾸기(replace)
a = " Life is too short"
a = a.replace("Live", "인생")
print(a)
a = a.replace("too", "넘나")
print(a)
#a = a.replace("Live","인생").replace("too","넘나")

# 문자열 나누기(split). 지정한 문자로 문자열을 나눈다.(리스트로 반환)
a = "a:b:c:d"
list1 = a.split(":")  # ["a","b","c","d"]
print(list1)
