
# 2단의 구구단을 가로 출력하는 프로그램을 만드시오. 끝날 때는 마침표를 붙인다.
# 힌트. 출력할 문자열을 변수에 저장하고 마지막 한번만 변수값을 print()를 사용하야 출력해야 한다.

# 방법1
for i in range(1, 10, 1):
    multiple2 = 2 * i
    if i == 9:
        print("2*", i, "=", multiple2, end=".")
    else:
        print("2*", i, "=", multiple2, end=",")

# 방법2
for i in range(1, 10, 1):
    str = "%s * %s = %s" % (2, i, 2*i)
    if i == 9:
        str = str + "."
    else:
        str = str + ","
    print(str, end=" ")
