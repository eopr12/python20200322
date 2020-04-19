#import 방식
# 1.import 모듈이름 -->같은 폴더에 있어야됨
# 사용방법:모듈명.함수명

# 2.from 모듈이름 import 모듈함수
# 사용방법:함수명

# 3.as import
import fibo

def main():
    # 사용방법:모듈명.함수명
    val = fibo.fib2(10)
    print(val)

# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()
# 이 두라인은 라이브러리 호출 마지막 단에 무조건 써라.
