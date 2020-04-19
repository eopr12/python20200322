############################
# 리스트의 CRUD2S 사용법을 익힌다.
# 리스트에 담을 수 있는 것은? ==> 다
# 리스트 선언 ==> [] , list()
# 리스트 추가(C) ==> .append(), .insert()
# 리스트 읽기(R) ==> [방번호]
# 리스트 수정(U) ==> [방번호] = 값
# 리스트 삭제(D) ==> .pop()
# 리스트 정렬(S) ==> sorted()
# 리스트 정렬(S) ==> .find() + 반복문 , .rfind() + 반복문
# 리스트 길이    ==> len()
############################
방번호 = 0
value = ""

#  List 선언
리스트 = []

#  C: 추가. 검색: "파이썬 리스트 추가"
#  append() 또는 insert()
#  MILK, BREAD, BUTTER 순으로 추가
리스트.append("MILK")
리스트.append("BREAD")
리스트.append("BUTTER")
print(리스트)

리스트.insert(0, "MILK").insert(1, "BREAD").insert(2, "BUTTER")

print(리스트)
#  APPLE 삽입. 검색: "파이썬 리스트 삽입"
#  특정 위치에 추가하기
#  "BREAD" 앞에 "APPLE" 삽입
위치 = 리스트.index("BREAD")
리스트.insert(위치, "APPLE")
print(리스트)

#  R: 읽기
#  BUTTER 값을 출력하시오.
#  "BUTTER" 가 들어있는 방번호 찾기
방번호 = 리스트.index("BUTTER")
print(리스트[방번호])

#  U: 수정. 검색: "파이썬 리스트 수정"
#  "BREAD" 를 "GRAPE"로 변경
#  "BREAD" 가 들어있는 방번호 찾기
리스트.replace("BREAD", "GRAPE")
방번호 = 리스트.index("BREAD")
print(리스트[방번호])

#  D: 인덱스로 삭제. 검색: "파이썬 리스트 삭제"
#  인덱스를 이용하여 GRAPE 를 삭제
#  "GRAPE" 가 들어있는 방번호 찾기


#  D: 값으로 찾아서 삭제. 검색: "파이썬 리스트 값으로 삭제"
#  값으로 MILK를 찾아서 삭제하시오


#  P: 리스트를 for문으로 출력.
#  검색: "파이썬 리스트 for 출력"
#  검색: "파이썬 리스트 크기"


#  테스트용 데이터 생성을 위한 코드. 수정하지 마시오.
print(리스트)  # ['APPLE', 'BUTTER']
for i in range(4):
    리스트.append("APPLE")
    리스트.append("BANNA")

# 도전.
#  첫번째 APPLE이 있는 방번호를 출력하시오.


#  S: 오름차순 정렬. 검색: "파이썬 리스트 오름차순 정렬"

#  S: 내림차순 정렬. 검색: "파이썬 리스트 내림차순 정렬"

#  APPLE 이 몇개 있나요?

#  리스트 의 모든 값을 while 문을 사용하여 삭제하시오
