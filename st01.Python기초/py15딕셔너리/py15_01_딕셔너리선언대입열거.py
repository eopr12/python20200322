# 리스트에서 key는 ==> [방번호]
# 딕셔너리에서는 key를 통해 value를 얻음 ==>{방 번호가 아닌 ""이름""}
#  금액: 얼마 / 폰번호: 010~ / 생일:ㅇㅇ월 ㅇㅇ일
# csv파일이나 엑셀파일로 만들기 위해서 주로 딕셔너리를 리스트안에 넣는 구조로
# 딕셔너리는 거의 리스트와 동일하다고 봐도 무방함

# 딕셔너리의 CRUD2S 사용법을 익힌다. 
# 딕셔너리에 담을 수 있는 것은? ==> 다
# 딕셔너리 선언 ==>  dic = { }
# 딕셔너리 추가(C) ==> dic["key값"] = "값" #없으면 만든다
# 딕셔너리 읽기(R) ==> dic["key값"]
# 딕셔너리 수정(U) ==> dic["key값"] = "값" #있으면 바꾼다
# 딕셔너리 삭제(D) ==> dic.pop("key값")
# 딕셔너리 정렬(S) ==> 없음. 왜냐하면 순서가 없기 때문
# 딕셔너리 검색(S) ==> 반복문 
# 딕셔너리 길이    ==> len(dic.keys() ) , len(dic.values() ) ,


# 딕셔너리 선언하기
# 사전 = {}
사전 = {
    "name": "망고",
    "type": "당",
    "ingredient": ["망고", "설탕", "소금", "치즈"],
    "origin": "필리핀",
}

# 딕셔너리 전체 내용을 출력해봅니다.
print(사전)

# R: 요소 추가 전에 내용을 출력해봅니다.
# 1. 선택 연산자를 사용하는 방법 ==> name, type값 출력
# 2. get() 메서드를 사용하는 방법 ==> ingredient, origin값 출력
# get방식은 key값이 없어도 무조건 출력해주기때문에 유용할 수 있음
print(사전["name"])  # key=name 값 출력
print(사전["type"])  # key=type 값 출력
print(사전.get("ingredient"))  # key=ingredient 값 출력
print(사전.get("origin"))  # key=origin 값 출력


# C: 딕셔너리 추가
# dictionary의 key head에 body 를 추가하고 값을 출력하시오
사전["head"] = "body"

print(사전)
print(사전["head"])
print(사전.get("head"))
# 사전.keys()
# 사전.valus()

# U: 딕셔너리 수정
# name 값을 "8D 망고" 로 수정하시오.
print(사전["name"])  # 망고
사전["name"] = "8D 망고"
print(사전["name"])  # 8D 망고

# D: 딕셔너리 삭제.
# 1. 연산자 방식 ==> del . 비추천
# 2. 메서드 방식 ==> .pop("key"). 추천
# name, type 키를 삭제
print("삭제전", 사전)
사전.pop("name")  # 방이름:name 삭제
사전.pop("type")  # 방이름:type 삭제
print("삭제후", 사전)

# S: 정렬. 딕셔너리는 정렬하는 방법이 없다. 왜냐하면 순서(방번호)가 없기 때문에
# 단, key 값 value 값만 개별적으로 정렬하는 것은 가능하다.(타입이 같아야만 정렬 가능)
# key 만 열거. keys() 메서드 사용.
# value 만 열거. values() 메서드 사용.

# S: 검색. 특별하는 방법이 없다.
# 선택연산자를 사용하면 바로 검색 되기 때문
# 사전["name"] 이런식으로 검색

# 존재하지 않는 키: 선택 연산자로 없는 키에 접근하면 에러 발생.
# try ~ except 를 추가하시오.
# KeyError
# 1. 선택 연산자를 사용하는 방법
try:
    name = 사전["name"]  # 사전에는 name 키값이 없어서 에러가 난다.
except KeyError as ex:
    print("KeyError", ex)
except Exception as ex:
    print("Exception", ex)

# 2. get() 메서드를 사용하는 방법
name = 사전.get("name")  # get메소드는 "사전"에 name 키값이 없어도 에러는 안나고 None으로 반환됨
print("name", name)

# 3. in 연산자를 사용하는 방법
if "name" in 사전:
    print("키 존재")
    name = 사전["name"]

else:
    print("키 없음")
    name = None
print("name", name)
###################
# 딕셔너리 열거
for i in 사전:
    print(i)
    print(type(i))  # class <str>
    print("사전열거", i, 사전[i])  # i는 키값 사전[i]는 value값

# 리스트열거랑 비교
for i in [1, 2, 3, 4]:
    print("리스트열거", i)  # i는 키값

# key 만 열거. keys() 메서드 사용.
for i in 사전.keys():
    print("keys()>>", i)

# value 만 열거. values() 메서드 사용.
for i in 사전.values():
    print("values()>>", i)

# key 와 value를 쌍으로 열거. items() 메서드 사용.
##################
for i in 사전.items():
    print(i)  # i는 튜플(읽기 전용 리스트)이다.
    print("items()>>", i[0], i[1])  # i는 튜플(읽기 전용 리스트)이다.

# key, value를 쌍으로 열거. items() 메서드 사용.

###################
# 딕셔너리 정렬
# kye만 정렬. keys().메소드 사용
keys = list(사전.keys())

print("keys 정렬 전", keys)
keys.sort()
print("keys 정렬 후", keys)

# value만 정렬. values().메소드 사용
values = list(사전.values())

print("values 정렬 전", values)
values.sort()  # value 타입이 달라서 에러가 나는게 정상
print("values 정렬 후", values)
