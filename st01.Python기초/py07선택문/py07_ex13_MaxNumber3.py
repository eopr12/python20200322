integer1 = int(input("입력하세요"))
integer2 = int(input("입력하세요"))
integer3 = int(input("입력하세요"))

if (integer1 > integer2) and (integer1 > integer3):
    print("입력받은 수중 가장 큰 수는", integer1, "입니다.")

elif (integer2 > integer1) and (integer2 > integer3):
    print("입력받은 수중 가장 큰 수는", integer2, "입니다")

else:
    print("입력받은 수중 가장 큰 수는", integer3, "입니다.")


# elif (integer3 > integer1) and (integer3 > integer2):
# print(integer3)

# 리스트,튜플,세트일 때에는 max함수로 구할 수 있음
# 딕셔너리는 사용하기는 좀 애매

list1 = [integer1, integer2,  integer3]
print("입력받은 수중 가장 큰 수는", max(list1), "입니다.")



if integer1 > (integer2 and integer3):
    print("입력받은 수중 가장 큰 수는", integer1, "입니다.")

elif (integer2 > integer1) and (integer2 > integer3):
    print("입력받은 수중 가장 큰 수는", integer2, "입니다")

else:
    print("입력받은 수중 가장 큰 수는", integer3, "입니다.")