# 500과 1000 사이에 있는 홀수의 합계 : 187500


sum = 0
for i in range(500, 1001, 1):
    if i % 2 != 0:
        sum = sum + 1
    else:
        pass
        print(sum)

# 정수 값을 입력받고
# 1부터 100까지 합계

sum = 0
int1 = int(input("정수값을 입력하세요."))
for i in range(1, int1+1, 1):
    sum = sum + 1
    print(i)

# 시작값, 끝값 그리고 증가값을 입력 받고
# "시작값"부터 "끝값"까지의 합계를 구하시오.
# 출력 예시)
# 시작값을 입력하세요: 2
# 끝값을 입력하세요: 300
# 증가값을 입력하세요: 3
# 1에서 300까지 3씩 증가시킨 값의 합계 : 15050

start = int(input("시작값을 입력하세요."))
end = int(input("끝값을 입력하세요."))
ascend = int(input("증가값을 입력하세요."))

sum = 0
for i in range(start, end+1, ascend):
    sum = sum + i
    # 1에서 300까지 3씩 증가시킨 값의 합계 : 15050
    print("%s에서 %s까지 %s씩 증가시킨 값의 합계 : %s" % (start, end, ascend, sum))


# "1에서 300" 까지 라는 문자열을 만드시오
str1 = "1에서 300"
print(str1)  # 1에서 300

# 이렇게 일일히하면 번거로움
시작값 = 1
끝값 = 300
str2 = str(start) + "에서" + str(end) + "까지"
print(str2)  # 1에서 300

str2 = "%s에서 %s까지" % (start, end)
print(str2)  # 1에서 300
