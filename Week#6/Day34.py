"""----------Day34----------"""
def FN1(group) :
    for x in group :
        print(x)

litters = [ 'A' , 'B' , 'C' ]
FN1(litters)#replace group with litters then do 'for' loop

def FN2(x) :
    return 3 * x

print(FN2(2))#do FN2 but replace x with 2 and return
print(FN2(4))
print(FN2(6))

def FN3(boy1 , boy2 , boy3) :
    print("the oldest boy is " , boy3)
#print value of boy3 which is hmedo
FN3(boy1="Ahmed" , boy2="khaled" , boy3="hmedo")

def FN4(*boy) :
    print("the youngest boy is " , boy[0])
#print value of boy indes 0  which is Ahmed
FN4("Ahmed" , "khaled" , "hmedo")

def rec(x) :
    if (x>0) :
       Ans = x+rec(x-1)
       print(Ans)
    else :
        Ans = 0
    return Ans
#rec(x-1) to recall fn.
print("\n\nRec Ex Ans")
rec(6)

    
    
