"""----------Day15----------"""
List1 = [ 'first' , 'second' , 'third', 'fourth' ]
List1.append('fifth')#put 'fifth' in last of the list
List1.insert(0, 'zero') #put 'zero' with index 0
List1.remove('second')#delete 'second' from the list
List1.pop(2)#delete index 2 which is 'third'
print(List1)
#delete all items
List2 = [ 'first' , 'second' , 'third', 'fourth' ]
List2.clear()
print(List2)
#to copy or make list
List3 = [ 'first' , 'second' , 'third', 'fourth' ]
List4 = List3.copy()#one way to copy
List5 = list(List3)#another way to copy
List6 = list(( 'A' , 'B' , 'C' , 'D' ))#also use list() to make new list
print(List4)
print(List5)
print(List6)
