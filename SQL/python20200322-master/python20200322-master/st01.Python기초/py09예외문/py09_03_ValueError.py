# Traceback (most recent call last):
#   File ".\py08_ValueError.py", line 2, in <module>
#     int("안녕하세요")
# ValueError: invalid literal for int() with base 10: "안녕하세요"

while True:
    try:
        n = input("숫자를 입력하시오 :  ")
        n = int(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오. ")

print("정수 입력이 성공하였습니다!")
