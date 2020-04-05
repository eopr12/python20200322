# print 들여쓰기 하냐 안하냐의 차이
# 하냐>결과값이 한번만 출력됨
# 안하냐>결과값이 일일이 하나씩 출력됨

sum = 0
for i in range(0, 11, 1):
    sum = sum + i
    print(sum)

###########################
# 0부터 9까지의 합계를 구하시오
sum = 0
for i in range(0, 10, 1):
    sum = sum + i
    print(sum)

###########################
# 문제. 0부터 100까지 짝수의 합계를 구하시오
sum = 0
for i in [0, 101, 1]:
    # i가 짝수이면 sum하고 아니면 pass
    if i % 2 == 0:
        sum = sum + i
    else:
        pass
    print(sum)
