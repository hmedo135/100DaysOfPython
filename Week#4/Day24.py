"""----------Day24----------"""
dict1 = {'name': 'hmedo', 'old': 23, 'phone': 966507720830, 'weight': 25}
dict2 = dict1.copy() #copy dict1 to dict2
dict3 = dict(dict1) #another method to copy
print(dict2)
print(dict3)
#if you use dict1 = dict2 to copy then
#any change will happen with dict1 also will happen with dict2

FamilyDict1 = { 'brother1' : { 'name' : 'mohammed' , 'old' : 18 } ,
                             'brother2' : { 'name' : 'hmedo' , 'old' : 23 } ,
                             'sister' : { 'name' : 'layan' , 'old' : 8 } }
print(FamilyDict1) #create 3 in 1 Dict

bro1 = { 'old' : 18 }
bro2 = { 'old' : 23 }
sis = { 'old' : 8 }
FamilyDict2 = { 'bro1' : bro1 ,
                             'bro2' : bro2 ,
                             'sis' : sis }
print(FamilyDict2) #add 3 in 1 Dict

    
dict4 = dict( name = 'hmedo' , old = 23 , phone = 966507720830, weight = 25 )
#use = instead of : also don't use ' ' with keys 
print(dict4) # to make a new dictionary
