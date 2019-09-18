'''----------Day14----------'''
#if you want print specific value , use its index position
MyList = [ 'x' , 'y' , 'z' , 3 , 4 , 5 ]
print(MyList[ 1 : 4 ])
#to check if it's in the list or not ,
#if you use in and it's not in actully will not print
MyList2 = [ 'x' , 'y' , 'z' , 3 , 4 , 5 ]
if 'A' not in MyList2:
    print("No 'A' is in the MyList" )
if 'x' in MyList2:
    print("Yes 'x' is in the MyList" )
#to repeat an item in the list use *
MyList3 = [ 'x' , 'y' , 'z' , 3 , 4 , 5 ] * 2
print(MyList3)
#you can add two list in one
MyList4 = [ 'A' , 'B' , 'C' , 0 , 1 , 2 ]
MyList5 = [ 'x' , 'y' , 'z' , 3 , 4 , 5 ]
MyList6 = MyList4 + MyList5
print(MyList6)
