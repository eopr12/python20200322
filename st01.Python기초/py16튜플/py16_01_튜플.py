

# 튜플 = 변경할 수 없는 리스트
# 읽기 전용 리스트를 만들고자 할 때 사용하면 된다.
# 함수에서 리턴을 여러개 받고자 할 때
# 변수 swap할 땐

# 리스트의 함수,연산자 동일
# 튜플은 [] 가아니라 ()

student1 = ("철수", 19, "CS")
print(type(student1))  # class 'tuple'

(name, age, major) = student1
print(name, age, major)

# 종종 튜플에서 괄호가 생략되기도 함
name1, age1, major1 = student1
print(name1, age1, major1)

# 이메일을 입력 받고 @를 기준으로 id와 도메인을 분리하는 프로그램을 작서하시오.
# 예시) abc@naver.com  --> id: abc  , domain: naver.com
이메일 = "abc@naver.com"
(id, domain) = 이메일.split("@")  # 양쪽의 갯수가 같아야 한다.
print("이메일", 이메일)
print("id", id)
print("domain", domain)
