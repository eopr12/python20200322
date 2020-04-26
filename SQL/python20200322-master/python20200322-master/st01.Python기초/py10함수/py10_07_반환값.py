# 함수 반환값


def get_sum(start, end):
    sum = 0
    for i in range(start, end, 1):
        sum = sum + i

    return sum


value = get_sum(1, 10)


def max(a, b):
    result = 0
    if a > b:
        result = a
    else:
        result = b
    return result
