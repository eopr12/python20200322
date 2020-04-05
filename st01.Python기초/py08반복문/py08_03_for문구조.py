# ~부터 ~까지
# 열거>리스트,딕셔너리에 있는 모든 값을 출력하시오.

# 열거
for name in ["철수", "영희", "길동", "유신"]:
    print("안녕", name)

# 모든 종류 안에 들어갈 수 있음
for x in [1, "a", True, None, ["가"]]:
    print(x, end=",")

# 문자열 자체도 리스트가 될 수 있음
for x in "abcd faoa":
    print(x, end=",")
