# 왜 반복을 사용하나?


# 순차문
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("환영합니다")
print("환영합니다")

# for 문
# for x in range(0, 10, 1):
#       문장
#       문장
# 읽는 방법:
# x는 0부터 10 전 까지; x를 1씩 올리면서
for x in range(0, 5, 1):
    print("환영합니다")

# while 문
# 조건식이 false일 때까지 반복
i = 0
while i < 5:
    print("환영합니다")
    count = i + 1

# 루프 탈출
# 조건식이 false가 되는 경우
# break가 사용되는 경우
# 무한실행 됐을 때 도스창 x누르거나 cntrl + C
