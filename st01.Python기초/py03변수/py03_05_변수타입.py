# Variables of different types

# 기본형 타입
b = True #불린
i = 1 #숫자
f = 0.1 #숫자
str = "Hello" #문자열
n = None #None "값이 없음"

# 변수 타입 확인
print( b, type ( b ) )
print( i,  type ( i ) )
print( f, type ( f ) )
print( str, type ( str) )
print( n, type ( n ) )

# 복합형 타입
l = [ 0, 1, 2, 0, 3 ] #리스트 : 중복 가능 배열
d = { 0 : "Zero", 1: "One" } # 사전:
t = (0, 1, 2) #튜플 : 읽기 전용 배열
set1 = set( [1, 2, 3, 1, 2] ) #세트 : 중복 불가 배열
set2 = set( "Hello" ) #세트 : 중복 불가 배열

# 변수 타입 확인
print( l , type ( l ) )
print( d, type ( d ) )
print( t, type ( t ) )
print( set1, type ( set1 ) )
print( set2, type ( set2 ) )