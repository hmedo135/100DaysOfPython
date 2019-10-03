"""---------Day31----------"""
def FN1(): 
    print('Surprise every one ^_^')
    #save print() inside FN1()
FN1() #Call FN1()
FN1()
#I can Call many time any time any where

def FN2(name = 'Unnamed'): 
    print('I am ' , name)

FN2()
#empty parameters will fill by Unnamed by Default
FN2('Abdulhameed')
FN2('Ahmed')
FN2('Khaled')
