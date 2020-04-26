def swap( list1 ):
    # a-->list1[0]
    # b-->list1[1]
    temp = list1[1]
    list1[1] = list1[0]
    list1[0] = temp
    print('swap 안: list1[0]=',list1[0], ', list1[1]=', list1[1])


def main():
    # 리스트 만들기 
    list1 = [5,3]  

    print('swap 전: list1[0]=', list1[0], ', list1[1]=', list1[1])
    swap(list1)
    print('swap 후: list1[0]=', list1[0], ', list1[1]=', list1[1])

main()