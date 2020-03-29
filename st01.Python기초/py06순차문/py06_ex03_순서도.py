# 이 순서도에는 오류가 있다
# 이렇게 예외가 발생하면 어떻게 처리해야 되나?
# 페이지 222~224 참조
# 코드의 처음부터 끝까지 감싸서 오류를 미연에 방지

try:

    s = input("s 입력")

    m = s // 60

    s = s % 60

    print(m, s)

except TypeError as identifier:
    print(identifier)


print("종료")