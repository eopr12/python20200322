value1 = input("첫 번째 과목 점수를 입력하세요")
value2 = input("두 번째 과목 점수를 입력하세요")

value1 = int(value1) // 문자열 value1 을 정수로 변환. 형변환
value2 = int(value2) // 문자열 value2 을 정수로 변환. 형변환

sum = value1 + value2
average = sum / 2

print("--------------")
if average >= 95 :
        print ("very Good")
else:
        print ("just Good")
print("--------------")