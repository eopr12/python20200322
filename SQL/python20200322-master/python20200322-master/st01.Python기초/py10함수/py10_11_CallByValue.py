def swap(a, b):
    # a-->b, b-->a
    temp = b
    b = a
    a = temp
    print('swap 안: a=', a, ', b=', b)


def main():
    # 변수의 선언과 초기화
    a = 5
    b = 3

    print('swap 전: a=', a, ', b=', b)
    swap(a, b)
    print('swap 후: a=', a, ', b=', b)

main()