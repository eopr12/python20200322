
#  /file/proverbs.txt 파일에서 줄 단위로 읽어서 output.txt 에 쓰시오

import os


def getAbsFileName(fileName):
    result = ""
    absfile = os.path.abspath(__file__)  # 스크립트 파일의 절대 경로
    curDir = os.path.dirname(absfile)  # 스크립트 폴더의 절대 경로
    txtA = os.path.join("/", fileName)  # ==> "/phones.txt"
    result = os.path.normpath(curDir + txtA)  # ==>절대경로

    return result


# 파일 열기
readfile = getAbsFileName("/file/proverbs.txt")
pfr = open(readfile, "r", encoding="utf-8")  # 읽기용 파일열기
writefile = getAbsFileName("/output.txt")
pfw = open(writefile, "a", encoding="utf-8")  # 쓰기용 파일뎔기

# 파일처리
# proverbs.txt에서 줄 단위로 읽어들여 output.txt 파일에 쓴다.
읽기 = pfr.readline()  # readline()에는 줄바꿈이 들어있어서 나중에 줄바꿀 필요 없음

while 읽기 != "":
    pfw.write(읽기)
    # pfw.write("\n")  # 줄바꿈
    읽기 = pfr.readline()

    # 파일 닫기
pfr.close()  # 읽기용 파일닫기
pfw.close()  # 쓰기용 파일닫기
