
# 교재 222-228페이지

# 숫자가 아닌 것을 정수로 변환하려고 할 때

# 숫자가 아닌 것을 실수로 변환 할 때

# 소수점이 있는 숫자 형식의 문자열을 int() 함수로 변환하려고 할 때

# IndexError

입력값 = int(input("숫자를 입력하세요."))  # 입력값 = "abc"이면 에러 발생

try:

    입력값 = int(input("숫자를 입력하세요."))  # 입력값 = "abc"이면 에러 발생
    입력값 = float(input("숫자를 입력하세요."))  # 입력값 = "abc"이면 에러 발생
    입력값 = int(input("숫자를 입력하세요."))  # 입력값 = "12.3"이면 에러 발생

except TypeError as ex:
    print("TypeError", ex)

except ZeroDivisionError as ex:
    print("ZeroDivisionError", ex)

except Exception as ex:  # TypeError도 아니고 아무것도 아니면 무조건 Exception에 넣어야 됨 > 무조건 마지막줄에 넣어야 됨
    print("Exception", ex)

# 테스트 방법
# 테스트1: abc입력
# 테스트2: 숫자0입력
# 테스트3: 숫자12.5입력
# 테스트4: 숫자12입력

# 함수코드를 try - except 구문 코드로 감싼다

# 오류 종류:컴파일 오류(구문 에러), 실행 오류(run-time error), 논리오류(logical error)

# Unhandled Exception : 0으로 나누는 경우 / 원격 데이터 접속시 연결 안되는 경우 / 파일 열었는데 삭제된 경우
