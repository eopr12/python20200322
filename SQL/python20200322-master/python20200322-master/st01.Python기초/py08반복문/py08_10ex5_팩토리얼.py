
입력값 = input("정수를 입력하시오:")
입력값 = int(입력값)

fact = 1
for i in range(1, 입력값+1, 1):
    fact = fact*i

str1 = "%s !은 %s 입니다 " % (입력값, fact)
print(str1)
