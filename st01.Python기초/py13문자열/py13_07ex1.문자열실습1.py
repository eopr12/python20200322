
#################################
# 문자열 함수 / 문자열 메서드
# len(), replace(), find() , split() 메서드의 사용법을 익혀본다.
#################################

# 0번째부터 12번째 자리까지 있음.
# prov 길이는 13이다.
prov = "A barking Dog"


# prov의 길이를 출력하시오. 문자열 길이: len().
a = len(prov)
print(a)

# 첫번째 b 문자를 찾고 위치를 출력하시오.
# 위치 찾는 메서드: find(), index()
a = prov.find("b")
print(a)

# 문자열에 "Dog"가 있으면 "Dog있음"을 없으면 "Dog없음" 을 출력하시오
# "Dog있음"
if prov.find("Dog") >= 0:
    print("Dog 있음")
else:
    print("Dog 없음")

# prov 문자열에 Dog가 들어 있으면 Cat으로 바꾸어 출력하시오.
if prov.find("Dog") >= 0:
    a = prov.replace("Dog", "Cat")
    print(a)


# 문자열 prov 를 공백을 기준으로 자르고 그 결과를 출력하시오.
# split() 가 반환 값은 리스트다
a = prov.split(" ")
print(a)
