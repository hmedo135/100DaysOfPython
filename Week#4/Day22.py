"""----------Day22----------"""
#dictionary 
dict1 = { 'name':'hmedo' , 'old':24 , 'phone':966507720830 , 'car':'toyota' }
print(dict1)
print(dict1['name'])#first method to print specific value
print(dict1.get('phone'))#second method to print specific value

dict2 = { 'name':'hmedo' , 'old':24 , 'phone':966507720830 , 'car':'toyota' }
print(dict2)
dict2['old'] = 23 #change specific value
print(dict2)

#for loop to print keys & values
dict3 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 }
print('---keys---')
for x in dict3:
    print(x) #print keys
print('---values---')    
for x in dict3:
    print(dict3[x]) #print values
#for x in dict3.values() :
   #print(x)
#also you can use to print values

#to print both keys & values
dict4 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 }
print('---keys---values---')
for x , y in dict4.items():
    print(x , y)
