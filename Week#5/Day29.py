"""----------Day29----------"""
set1 = ["Welcome" , "Hello !" , "bye"]
for x in set1:#put all items in x to print
    print(x)

for x in "Python": print(x)
#print litters

set2 = ["Welcome" , "Hello !" , "bye"]
print("---break with 'Hello !'---")
for x in set2 :
    print(x)#break with Hello !
    if x == "Hello !" :
        break
print("---break without 'Hello !'---")
for x in set2 :
    if x == "Hello !" :
        break
    print(x)#break without Hello !

set3 = ["Welcome" , "Hello !" , "bye" , "Good"]
for x in set3 :
    if x == "bye" :
        continue #skip 'bye'
    print(x)
