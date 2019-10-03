"""----------Day28---------"""
#While Loop will end in 100
A = 0
while A <= 100 :
    print("This Time A = " , A)
    A += 20

B = 1.0
while B < 6.0 :
    print("Get Out If B = 3.0 , Now B = " , B)
    if B == 3.0 :
        break #if B = 3.0 will not keep going
    B += 0.5
    
C = 0
while C < 6 :
     C += 1
     if C == 3 :
          continue #if C = 3.0 will skip loop
     print("If C = 3 It Will Skip Printing This  , Now C = " , C)

x = 1
while x < 6 :
    print(x)
    x += 1
else :# do this when get out of loop
    print("Now, x is more than 5")
