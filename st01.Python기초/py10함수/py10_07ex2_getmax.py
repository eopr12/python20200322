# 사용자 함수 만들기
# 두 개의 정수가 주어지면 두수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수를 만들어보자.

# 함수 정의
# x : 매개변수
# y : 매개변수

# 왜 main() 함수를 만들어 사용하는가?
# 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다


def get_max(x, y):
    result = None
    # try 최댓값 = max(get_max) except 안되나?

    # list1 = [ 정수1, 정수2 ] >>>>리스트로 먼저 묶고나서 max함수 써도 됨

    # result = max( list1 )
    try:
        if(x > y):
            result = x
        else:
            result = y
    except Exception as ex:
        pass

    return result


# main함수 호출 = 프로그램의 시작점이 된다.
def main():

    result = None

    첫번째정수 = newmethod535("첫번째")
    두번째정수 = newmethod535("두번째")

    value = get_max(첫번째정수, 두번째정수)
    print(value)

    value = get_max(10, "20")  # value값은 무엇일까요? ==>None
    if(value == None):
        print("error이므로 다시 입력하세요.")
    else:
        print(value)

    return result

# 반복되는 코드 함수화


def newmethod535(x):
    정수 = None
    try:
        str = x + "정수 입력: "  # 첫번째 정수 입력:
        i = input(str)
        정수 = int(i)  # ㅇ번째 매개변수처리
    except Exception as ex:
        pass

    return 정수


main()

# 메인함수는 return하지 않는다. 프로그래밍에서 지향하는 방식은 전역변수를 사용하지 않는다.
# value는 메인함수의 지역변수
