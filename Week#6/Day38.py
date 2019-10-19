"""----------Day38---------"""

cars1 = ['Toyota' , 'BMW' , 'Ford' , 'GMC']
for x in cars1 :
    print(x)

cars2 = ['Toyota' , 'BMW' , 'Ford' , 'GMC']
cars2.append('Honda')#add Honda at the end
print(cars2)

cars3 = ['Toyota' , 'BMW' , 'Ford' , 'GMC']
cars3.pop(0)
print(cars3)
cars3.remove( 'Ford' )
print(cars3)
