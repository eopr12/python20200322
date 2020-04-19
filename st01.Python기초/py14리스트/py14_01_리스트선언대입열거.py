
# 변수 = 단독주택
# 리스트(배열) = 아파트(변수들을 모아놓은 것)

###########################
# 리스트의 CRUD3S
# C: create. / .append(*), .insert()
# R: read / [방번호]
# U: update / [방번호] = 값
# D: delete / .pop()
# S: search / sfind+반복문, rfind()+반복문
# S: sort / .sorted()
# S: shuffle
############################


############################
# 리스트 선언
# 리스트에는 다 담을 수 있다. 함수도 담을 수 있다.
############################

def func():
    print("함수")


# 리스트 만드는 방법1
array = []
# 리스트 만드는 방법2
array = list()
array = [None, 1, 1.1, "문자열", True, [], {}, func]
array[-1]()  # "함수" ()는 함수 호출한거임

############################
# 문자 H, e, l, l, o를 요소로 가지는 리스트
# 문자열 Hello를 요소로 가지는 리스트
# 문자열을 리스트로 변환. 문자 H, e, l, l, o를 요소로 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
# 0, 1, 2, 3, 4를 요소가 가지는 리스트 생성
############################
# 리스트 만드는 방법1
list1 = ["H", "e", "l", "l", "o"]
print(list1, type(list1))
# 리스트 만드는 방법2
list2 = list("Hello")
print(list2, type(list2))

list3 = ["Hello"]
print(list3, type(list3))

list4 = ["0", "1", "2", "3", "4"]
print(list4, type(list4))

list5 = list("01234")
print(list5, type(list5))
############################
# 리스트 요소 출력
# 리스트의 시작은 0번부터다.
# 리스트  Read : [] 선택 연산자를 사용한다.
############################
array = [None, 1, 1.1, "문자열", True, [], {}, func]
print(array[0], type(array[0]))  # None, <class 'NoneType'>
print(array[1], type(array[1]))
print(array[2], type(array[2]))
print(array[3], type(array[3]))


############################
# 리스트 전체 출력
############################
print(array)

############################
# 리스트 슬라이싱 :
# 1. 선택 연산자 사용하는 방법.
############################


############################
# 리스트 요소 대입
# 리스트의 0번 값을 문자열 "변경"값으로 바꾸시오.
############################
array[0] = "변경"
print(array[0], type(array[0]))
print(array)

############################
# 리스트 요소 추가: C. create
#  추가 : 리스트의 마지막에 넣는다. --> .append() 메서드 사용
#  삽입 : 리스트의 중간에 넣는다.   --> .insert() 메서드 사용
############################
array = [None, 1, 1.1, "문자열", True, [], {}, func]
print(array)
array.append("추가")  # 리스트 마지막에 추가됨
print(array)
array.insert(0, "삽입")  # 원하는 위치에 삽입됨
print(array)

############################
# 리스트 요소 삭제: D. deletef
#  메서드 방식 --> pop() 메서드 . 추천
#  연산자 방식 --> del. 비추천
############################
array = [None, 1, 1.1, "문자열", True, [], {}, func]
array.pop(0)  # None이 사라짐
print(array)

############################
# 리스트 열거
############################
array = ["A", "a", "B", "b", "A", "a", "B", "b"]
for i in array:
    print(i, end = " , ")
print()
############################
# 리스트 정렬
############################
array = [None, 1, 1.1, "문자열", True, [], {}, func]  # 타입이 섞여있어서 에러뜸
array.sort()
print(array)

array = ["A", "a", "B", "b"]
array.sort()
print(array)

array = ["C", "a", "b"]
array.sort()
print(array)
# 대문자-소문자 순으로 정렬됨

############################
# 리스트 검색
############################
array = ["A", "a", "B", "b", "A", "a", "B", "b"]
slist = []
for i in range(0, len(array), 1):
    pos = array.index("a", i)
    if pos >= 0:
        slist.append(pos)
        i = pos + 1
print(pos)

############################
# 리스트에 담을 수 있는 것은? ==> 다
# 리스트 선언 ==> [] , list()
# 리스트 추가(C) ==> .append(), .insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> .pop() / .remove() 원하는 값 지정해서 없앨 수 있음
# 리스트 정렬(S) ==> .sort(),  sorted()
# 리스트 검색(S) ==>.index() + 반복문
# 리스트 길이    ==> len()
# 리스트 출력
# 리스트 열거 ==> for문
############################
