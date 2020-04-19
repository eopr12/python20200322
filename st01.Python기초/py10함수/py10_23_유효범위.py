# 함수안에 함수 구조 가능(내부함수)


def foo():
    a = 3
    b = 5

    def bar():
        b = 7
        c = 11

        a = b + c
        print(a, b, c)  # 18 7 11

    print(a, b)  # 3, 5
    bar()
    print(a, b)  # 3, 5


foo()
