입력값 = int(input("정수를 입력하세요."))
fact = 1

for i in range(1, 입력값+1, 1):
    fact = fact*i

str1 = "%s !은 %s입니다" % (입력값, fact)
print(str1)
