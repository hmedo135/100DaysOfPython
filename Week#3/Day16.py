"""----------Day16----------"""

Tuple1 = ( 'cat' , 5 , 1.9 , 'man' )
print(Tuple1)#print all value
print(Tuple1[0])#print index 0
print(Tuple1[ 1 : 4 ])#print from index 1 to 3

Tuple2 = ( 'Dog' , ) #must use ( , ) if there one value
print(Tuple2)
Tuple3 = ( 'Dog' )#will print as a regular value not tuple
print(Tuple3)

Tuple4 = ( 'cat' , 5 , 1.9 , 'man' )
for x in Tuple4: #put all index inside x  using for loop
    print(x)
