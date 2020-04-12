# First num: 2
# Second Num: 4
# Add: 6 >>Add()함수 이용 / 매개변수 2개 사용 x,y
# Minus: -2 >>Minus()함수 이용
# Mul: 8 >>Mul()함수 이용
# Div: 0.500000 >>Div()함수 이용 / 주의:Zero DivisionError 처리


def Add(x, y):
    result = None

    try:
        result = x + y
    except Exception as ex:
        pass

    return result


def Minus(x, y):

    try:
        result = x - y
    except Exception as ex:
        pass

    return result


def Mul(x, y):

    try:
        result = x * y
    except Exception as ex:
        pass

    return result


def Div(x, y):

    try:
        result = x / y
    except ZeroDivisionError as ex:
        pass
    except Exception as ex:
        pass

    return result


def myinput():
    result = None

    try:
        result = int(input("입력하세요."))
    except Exception as ex:
        pass

    return result


def myprint(str, value):
    result = None

    try:
        result = "%s : %s" % (str, value)
        print(result)
    except Exception as ex:
        pass

    return result

# main함수는 함수들을 조합하는 역할을 담당(데이터 수집 + 처리 + 출력)
# main함수가 함수의 시작점이 된다.


def main():

    result = None

    # 첫번째 정수 입력 받기
    # 두번째 정수 입력 받기
    # Add함수 호출하고 결과값 출력
    # Minuis함수 호출하고 결과값 출력
    # Mul함수 호출하고 결과값 출력
    # Div함수 호출하고 결과값 출력
    첫번째정수 = myinput()  # ===>x
    두번째정수 = myinput()  # ===>y

    반환값 = Add(첫번째정수, 두번째정수)  # Add()함수 호출하고 결과를 반환값에 저장
    #출력 = "Add: %s" % (반환값)
    # print(출력)
    myprint("Add", 반환값)

    반환값 = Minus(첫번째정수, 두번째정수)
    myprint("Minus", 반환값)

    반환값 = Mul(첫번째정수, 두번째정수)
    myprint("Mul", 반환값)

    반환값 = Div(첫번째정수, 두번째정수)
    myprint("Minus", 반환값)

    return result


main()
