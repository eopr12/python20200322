# 2단의 구구단을 출력하는 프로그램을 만드시오
# 1부터 9까지 2단의 구구단을 출력하시오.
# range()함수를 사용한다.

for i in range(1, 10, 1):
    multiple2 = 2 * i
    print("2 *", i, "=", multiple2)
    str2 = "%s 에서 %s까지" % (1, 10)  # 문자열
    print(str2)


# 구구단 7단 단을입력하세요:7
multiplewhat = int(input("단을 입력하세요:"))
for t in range(1, 10, 1):
    multiplew = multiplewhat * t
    print(multiplewhat, "*", t, "=", multiplew)

multiplewhat = int(input("단을 입력하세요:"))
for t in range(1, 10, 1):
    multiplew = multiplewhat * t
    print(multiplewhat, "*", t, "=", multiplew)
