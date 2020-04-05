# py04_02_ifelse

# 하나의 점수를 입력 받고, 입력 받은 점수에 해당하는 학점을 출력하는 프로그램을 작성하시오.
# 입력 받는 정수는 0~100까지이고
# 90점 이상이면 A,
# 80점 이상이면 B,
# 70점 이상이면 C,
# 60점 이상이면 D,
# 나머지는 F

############################
# 비교 연산자와 논리 연산자 결합한 방법
grade = int(input("점수를 입력하세요"))
if 90 <= grade and grade <= 100:
    print("A")
elif 80 <= grade and grade < 90:
    print("B")
elif 70 <= grade and grade < 80:
    print("C")
elif 60 <= grade and grade < 70:
    print("D")
else:
    print("F")

############################
# 비교 연산자만 사용한 방법
grade = int(input("점수를 입력하세요"))
if 90 <= grade:
    print("A")
elif 80 <= grade:
    print("B")
elif 70 <= grade:
    print("C")
elif 60 <= grade:
    print("D")
else:
    print("F")


##반복문##

grade = input("grade :")  # 95

# grade는 0부터 100 사이의 값만 가능해야 한다.
while grade < 0 or 100 < grade:

    # 그 이외의 값이 들어오면 grade를 다시 입력 받게 작성하시오.
    grade = input("grade :")  # 95
    grade = int(grade)  # 95

    if 0 <= grade <= 100:
        # 반복문 종료
        break
    else:
        # 다시 입력 받는다.
        pass
