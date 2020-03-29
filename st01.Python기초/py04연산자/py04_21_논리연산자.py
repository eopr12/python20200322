x = 3
y = 4

r = ((x == 3) and (y == 3))  
print("( x == 3 ) and ( y == 3 ) : ", r)

r = ((x == 3) and (y != 3))
print("(x == 3 ) and ( y != 3) : ", r)

r = ((x == 3) or (y == 3))
print("( x == 3 ) or ( y ==3 ) : ", r)

r = ((x == 3) or (y == 4))
print("( x == 3) or ( y == 4 ) : ", r)
