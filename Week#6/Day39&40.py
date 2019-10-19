"""---------Day39&40----------"""
#Question 1
def rec( A , B ) :
    if (A > 0) :
       Ans = A ** B
       print(Ans)
    else :
        Ans = 0
    return Ans
print("\n\nWeek Challenge ^_^")
rec( 5 , 3)

#Question 2
list1 = [-4, -6, -5, -1, 2, 3, 7, 9, 88 ]
print(list1)
PosList = []
FN = lambda x : x > 0
for x in list1 :
    if FN( x ) :
        PosList.append( x )
print(PosList)

