
# swap이란? 변수의 값을 바꾸는 코딩 기법

# 1. 외팔이 swapm 방법. 모든 프로그래밍 언어에서 사용 가능
x = 2
y = 3

print("swap 전 : x, y =", x, y)
temp = x
x = y
y = temp
print("swap 후 : x, y =", x, y)

# 2. 튜플을 사용하는 swap 방법. 파이썬에서만 가능
x = 2
y = 3
print("swap 전 : x, y =", x, y)
(y, x) = (x, y)
print("swap 후 : x, y =", x, y)
