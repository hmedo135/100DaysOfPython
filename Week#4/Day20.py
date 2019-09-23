"""----------Day20----------"""
#repeated values can't be print
set1 = { 'Hello' , 'Yes' , 5 , 1 , 'Yes' , 3 , 5 }
print(set1)
#Loop through the set and print the values
set2 = { 'A' , 'B' , 'C' , 'D' }
for x in set2:
    print(x)
#Check if value is present in the set
set3 = { 'Hello' , 'Yes' , 5 , 1 , 3 }
print("Yes" in set3)
#add one value
set4 = { 'A' , 'B' , 'C' , 'D' }
set4.add("help")#add one value
print(set4)
#add many values
set4.update({ 'Hello' , 'Yes' , 5 , 1 , 3 })
print(set4)
