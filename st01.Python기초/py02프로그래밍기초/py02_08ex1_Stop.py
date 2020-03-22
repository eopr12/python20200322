# 디버깅을 이용하여 반복 되는 과정을 이해한다.
# 디버깅 : 버그를 잡는 행위
# breakpoint 지정
# F5 디버깅 시작 / F10 디버깅 종료,다음 줄 이동
# 주의사항!!! 줄 맞춤



sign = "stop"

while sign == "stop":

            sign = input("현재 신호를 입력하시오")
            print("입력값>>>", sign)

print("OK! 진행합니다.")
