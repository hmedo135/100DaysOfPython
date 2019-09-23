"""----------Day23----------"""
dict1 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 , 'car':'toyota' }
if 'old' in dict1: #check "old"
    print('Yes, "old" exist in dic1')
if 'year' not in dict1: #check "year"
    print('No, "year" not exist in dic1')
print(len(dict1)) #print number how many items?

dict2 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 }
dict2['weight'] = 52 #add 'weight':25 to dict2 
print(dict2)

dict3 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 , 'weight':25 }
print(dict3)
dict3.pop('phone') #delete "phone" item
print(dict3) 
dict3.popitem() #delete last item
print(dict3)

dict4 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 }
dict4.clear() #clear all items
print(dict4)
dict5 = { 'name':'hmedo' , 'old':23 , 'phone':966507720830 }
del dict5 #delet dict5 completely
print(dict5)
