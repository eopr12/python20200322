
#########################
# 키보드 입력을 파일에 쓰는 프로그램을 작성하여 본다.
#########################
import os

# 파일열기
pfw = open("phones.txt", "a", encoding="utf-8")

# 키보드 입력 받고 파일에 쓰기
입력값 = input("입력하세요.>>>")
pfw.write(입력값 + "\n")  # write()는 줄바꿈 안됨
# or pfw.write("\n")

입력값 = input("입력하세요.>>>")
pfw.write(입력값 + "\n")  # write()는 줄바꿈 안됨
# or pfw.write("\n")

입력값 = input("입력하세요.>>>")
pfw.write(입력값 + "\n")  # write()는 줄바꿈 안됨
# or pfw.write("\n")

# 파일닫기
pfw.close()

########################
# 입력값 반복되니까 반복문으로 바꾸기
# 파일열기
pfw = open("phones.txt", "a", encoding="utf-8")
# a = 없으면 만들고 있으면 추가됨
# w = 없으면 만들 수 있는데 있으면 중복으로 만들 수 없음

# 키보드 입력 받고 파일에 쓰기
while True:
    입력값 = input("입력하세요.>>> 입력을 끝내려면 엔터>>>")
    if 입력값 == "":
        break
    else:
        pfw.write(입력값 + "\n")  # write()는 줄바꿈 안됨
    # or pfw.write("\n")

# 파일닫기
pfw.close()
#########################


#########################
