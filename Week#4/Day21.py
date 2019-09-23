"""----------Day21---------"""
set1 = { 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' }
print(len(set1))#Get the number of values in a set1

set2 = { 'A' , 'B' , 'C' }
x = set2.pop()
print(x , ' is the deleted value')#print deleted value
print(set2)#print set after delete

#delete specific value
set3 = { 'A' , 'B' , 'C' , 'D' , 'E' }
set3.discard('B')
set3.discard('W')
set3.remove('C')
print(set3)
"""the diffrent between remove & discard is
if the value to remove does not exist,
￼remove() ￼will raise an error!"""
set3.remove('W')

set4 = { 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' }
set4.clear()#to empties the set4
print(set4)
set5 = { 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' }
del set5 #to delete the set completely
print(set5)

#to make a set
set6 = set(( 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' ))
print(set6)
