"""----------Day27----------"""
A , B = 5 , 10
if A > B :
    print('A greater than B') #print this if condition was TRUE
elif A == B : #check A==B if A>B was FALSE
    print('A and B are equal')
else : #if all past conditions was FALSE do this
    print('B greater than A')
    
#short methods all in one line
C , D = 20 , 30
if D > C : print('D greater than C')
print('C is the greatest') if C > D else print('D is the greatest')
print('C more than D') if C > D else print('D more than C') if  D > C else print('C and D are equal')

E , F = 40 , 50
if E == 40 and F > E : #all TRUE
    print('both conditions are TRUE')
if F == 100 or F > E : #F not equal 100 FALSE
    print('one of the conditions is TRUE') #both TRUE will not print

G = 1000
if G > 999 :
    print("Yes, of course it's over 999")
    if G == 1000 : # this (if) is inside first (if) because started space
        print("Yes, you got it, it's equal to 1000")
    else :
        print("No, not even close")
