# 데이터 수집
# readList 반환값은 리스트라고 가정
# 음수가 입력될 때까지 무한 입력 처리하고 리스트를 결과로 반환

# 코드작성
# 1. 무한루프 만들고
# 2. 키보드 입력받고 정수변환
# 3. 입력값이 음수이면 루프 탈출 아니면 리스트에 저장하고 반복한다.


def readList():
    result = None

    result = []  # 리스트생성

    while True:
        입력값 = int(input("숫자를 입력하세요."))

        if 입력값 < 0:
            break
        else:
            # 리스트에 추가
            result.append(입력값)

    return result

# 데이터 처리(작은 값부터 큰값 순으로 리스트를 정렬) / (nlist.sort())
# nlist : 리스트


def processList(nlist):
    result = None
    result = sorted(nlist)  # 오름차순으로 리스트를 정렬한다.
    return result

    # 데이터 출력(리스트의 값을 출력)


def printList(nlist):
    result = None
    for i in nlist:
        str = "성적: %s" % i
        print(str)
    return result

    # 프로그램 시작


def main():
    result = None

 # main 함수의 처리순서
    # 1. 데이터 수집===>readList() 함수 사용
    # 2. 데이터 처리===>processList() 함수 사용
    # 3. 데이터 출력===>printList() 함수 사용
    result = readList()  # 리스트가 반환됨
    result = processList(result)
    result = printList(result)

    return result


main()


# 이 모듈이 단독으로 사용되면 main()를 호출하라.
if __name__ == "__main__":
    main()
