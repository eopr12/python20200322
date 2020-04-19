# 모듈(파일1개)<패키지(디렉토리/모듈 여러개)<라이브러리(누군가가 배포해놓은거)<프레임워크(Ioc)
# Ioc(Inversion of Control)

#######################
# fibo 모듈 만들기
#######################

# fib(n) : 피보나치 수열의 결과를 반환하는 함수 만들기

# fib2(n) : 피보나치 수열을 리스트로 반환하는 함수 만들기


# 피보나치 수열 모듈

def fib(n):
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

# 피보나치 수열 모듈


def fib2(n):  # 피보나치 수열을 리스트로 변환
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


# main 함수가 없는 경우
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

# 커맨드에서 매개변수를 받는 방법은 배치에서 사용됨
# 배치: ex 월요일마다 ~ 해라


# 모듈 탐색경로
# 1.현재 디렉토리
# 2.PYTHONPATH디렉토리
# 3.설치 디렉토리
