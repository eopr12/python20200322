a = 1
b = 2
c = a + b

while c < 30:
    c = a + b
    a = b
    b = c

print(c)
