# 사용자 함수 만들기
# 일회용 패스워드 생성기를 이용하여서 3개의 패스워드를 생성하여 출력하는 프로그램을 작성해보자.

# 1.데이터 수집_리스트화,입력값받기


def newmethod359():  # 입력값이 2번이상 반복되서 함수화시킴
    result = None
    result = int(input("시작값을 입력하세요."))
    return result


def readList():

    result = None

    result = []  # 리스트화
    입력값 = newmethod359()
    result.append(입력값)  # 0번방에 저장

    입력값 = newmethod359()
    result.append(입력값)  # 1번방에 저장

    return result


# 2-1.데이터 처리_오름차순정렬


def processList(nlist):
    result = None

    result = sorted(nlist)

    return result

# 2-2.데이터 처리_합계


def sumList(nlist):
    result = 0  # 합계를 구하기 위해서 None 대신 0으로 초기화
    for i in nlist:  # 리스트 명으로 놓으면 하나씩 올라간다는 가정임 range써도 됨
        result = result + i  # i의 의미: i번째 방의 값이다.
    return result  # 합계값

# 반환되는 리스트는 이렇다===>(0번방:시작값 / 1번방:종료값 / 2번방:합계)

# 3.데이터 출력


def printList(nlist):
    result = None
    result = "%s부터 %s까지의 합계는 %s입니다" % (nlist[0], nlist[1], nlist[2])
    print(result)
    return result

# 4.프로그램 시작_함수정리 및 호출


def main():
    result = None

    result = readList()
    result = processList(result)  # 시작값, 종료값
    합계값 = sumList(result)
    # 합계값을 result에 추가하시오.
    result.append(합계값)  # result = [시작값, 종료값, 합계값]
    result = printList(result)  # 여기서의 result는 최종적으로 문자열이다.

    return result


main()
