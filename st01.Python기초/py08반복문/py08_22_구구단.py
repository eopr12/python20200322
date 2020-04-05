# 중첩 for문
for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        str1 = "%s * %s = %3s, " % (i, j, i*j)
        print(str1, end="")
    print()
