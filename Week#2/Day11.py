"""----------Day11----------"""
#for and if two conditions are correct print True
print("'---for and---'")
A = 3
print(A>2 and A>4)
print(A>2 and A<4)
print(not(A>2 and A<4))#for not print the reverse answer
#for or if one or two conditions are correct print True
print("'---for or---'")
print(A>2 or A>4)
print(A>2 or A<4)
print(not(A>2 or A<4))#for not print the reverse answer

x = ["Hello!"]#[ ]must be written 
y = ["Hello!"]
z = x
print(x is z)
print(x is not z)
print(x is y)
print(x is not y)
# is used compare if they are actually the same object,
#with the same memory location
print(x != y)
B = ["you","me"]#[ ]must be written 
print("me" in B)#is "me" inside B
print("me" not in B)


