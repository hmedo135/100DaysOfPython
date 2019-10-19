"""----------Day36---------"""

def FN1(n) :
    return lambda A : A * n
x = FN1(4)
print(x(5))#x(A)

def FN2(m) :
    return lambda B : B * m
x1 = FN2(3)
x2 = FN2(6)
print(x1(5))#x1(B)
print(x2(10))#x2(B)
