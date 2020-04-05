# 무한루프 루프탈출

while True:

    # py08_26 코드 복사
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

    int1 = int(input("정수를 입력하세요"))

    if int1 >= 0:
        pass
    else:
        break

    print(int1)
print("정상 종료합니다.")
