
# 파일 존재 여부 확인
# 현재 폴더에 phones.txt 파일이 존재하는지 확인한다.
# os.path.isfile() 메서는 있으면 True 없으면 False 를 반환한다.


import os  # 파일 처리 모듈

#########################


def getAbsFileName(fileName):
    result = ""
    absfile = os.path.abspath(__file__)  # 스크립트 파일의 절대 경로
    curDir = os.path.dirname(absfile)  # 스크립트 폴더의 절대 경로
    txtA = os.path.join("/", fileName)  # ==> "/phones.txt"
    result = os.path.normpath(curDir + txtA)  # ==>절대경로

    return result


#########################
fileName = getAbsFileName("/file/phones.txt")
# py21표준모듈에 있는 phones.txt를 가져오려면 ==>  "../py21표준모듈/phone.txt"

# 읽기 모드로 파일 열기, 이 때 encoding = "utf-8" 을 지정한다.
pfr = open(fileName, "r", encoding="utf-8")  # encoding 미지정 == ASCII코드로 자동

# readline() 파일에서 한 줄씩 읽기
value = pfr.readline()
print(value, end="")  # end=""한 이유는 줄바꿈 안하려고
value = pfr.readline()
print(value, end="")
value = pfr.readline()
print(value, end="")

# 파일 닫기
pfr.close()


#########################
# 반복문으로 파일에서 읽어서 모니터에 출력하기
# 읽기 모드로 파일 열기, 이 때 encoding 을 지정한다.


fileName = getAbsFileName("/file/phones.txt")
# py21표준모듈에 있는 phones.txt를 가져오려면 ==>  "../py21표준모듈/phone.txt"

# 읽기 모드로 파일 열기, 이 때 encoding = "utf-8" 을 지정한다.
pfr = open(fileName, "r", encoding="utf-8")  # encoding 미지정 == ASCII코드로 자동

# 파일에서 한 줄씩 읽기 : readline()
value = pfr.readline()
while value != "":  # 대충 값이 있을때만 돌아라라는 뜻
    print(value, end="")
    value = pfr.readline()


# 파일 닫기
pfr.close()
