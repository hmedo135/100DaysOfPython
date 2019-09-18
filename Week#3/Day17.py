"""----------Day17---------"""
#to be sure is value inside tuple?
Tuple1 = ( 'take' , 'give' , 'massage' , 'hi' )
if 'hi' in Tuple1:
    print('''Yes, 'hi' in Tuple1''')
if 'Hi' not in Tuple1:
    print('''No, 'Hi' not in Tuple1''')

Tuple2 = ( 'Hi !  ') * 5 #to repeat a tuple
print(Tuple2)
Tuple3 = ( '5' , '4' , '3' ) #to add a tuple
Tuple4 = Tuple3 + ( '3' , '2' , '1' )
print(Tuple4)

print(len(Tuple4)) #to calculate how much value in tuple

#to change from list or any type to tuple
list1 = [ 'a' , 'b' , 'c' , 'd' ]
Tuple5 = tuple(list1)
print(Tuple5)
