# 시작단수 종료단수 1 4
시작단수 = int(input("시작 단수를 입력하세요."))
종료단수 = int(input("종료 단수를 입력하세요."))

for i in range(11, 16, 1):
    for j in range(1, 10, 1):
        str1 = "%s * %s = %s" % (i, j, i*j)
        print(str1, end=",")
    print()

# 시작단수 종료단수 4 1 스위칭,스왑
시작단수 = int(input("시작 단수를 입력하세요."))
종료단수 = int(input("종료 단수를 입력하세요."))

# 1번방법 그냥 -1로해서 for문 두번쓰기
if 시작단수 > 종료단수:
    for i in range(시작단수, 종료단수-1, -1):
        for j in range(1, 10, 1):
            str1 = "%s * %s = %s" % (i, j, i*j)
            print(str1, end=",")
        print()
else:
    for i in range(시작단수, 종료단수-1, 1):
        for j in range(1, 10, 1):
            str1 = "%s * %s = %s" % (i, j, i*j)
            print(str1, end=",")
        print()

# 2번방법 스왑,스위칭
if 시작단수 > 종료단수:
    임시값 = 시작단수
    시작단수 = 종료단수
    종료단수 = 임시값

else:
    pass


for i in range(시작단수, 종료단수, 1):
    for j in range(1, 10, 1):
        str1 = "%s * %s = %s" % (i, j, i*j)
        print(str1, end=",")
    print()
