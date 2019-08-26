"""----------Day1----------"""
#How to print
print (" Hello, World !")
#How to exit
#exit()
#must be space befor print
if 4>2:
 print("hmedo")
"""----------Day2---------"""
 #Use hashtag(#) to write a comment
print("Hi !") #This is a comment
 #or to disable a command
 #print("Hi !")
"""for multi lines like this comment
use " three times at the beginning
and three times at the end
of the comment"""
"""----------Day3----------"""
#if you want to store data inside Variables
x = 5
y = "Hi !"
print(x)
print(y)
#you can write multiple variables in one line
x, y, z = "Apple", "Orange", "Banana"
print(x)
print(y)
print(z)
#you can add text with variable definded alraedy
x = "fine"
print("I'm " + x)
#you can add words or numbers ,word with number can't be add
x = "I'm"
y = "fine"
z = x + y
print(z)
A = 2
B = 3
C = A + B
print(C)
#D = x + A #Error can't be add
#print(D) #Error can't be print
"""----------Day4----------"""
#if you want to know what is the of any N.O.
A=10 #if it was -10 also will be (int)
print("The class type of A=10 is "+str( type(A)))
B = 0.1#if it was 10e4 , -10e4 or -100.e1 also will be (float)
print("The class type of B=0.1 is "+str( type(B)))
C = 1j#if it was -1j or 2+2j also will be (complex)
print("The class type of C=1j is "+str( type(C)))
#if you want to convert to specific type
A=10
a=float(A) #convert from (int)to(float)
print("The result of a is ",a,"& The class type is "+str(type(a)))
B = 1.9
b=int(B) #convert from (float)to(int)
print("The result of b is ",b,"& The class type is "+str(type(b)))
#*you con't convert from complex to other types 
C = 2
c=complex(C) #convert from (int)to(complex)
print("The result of c is ",c,"& The class type is "+str(type(c)))
#to  select random N.O.
import random
print(random.randrange(0,4))
"""----------Day5----------"""
#Exercise
x , y , z = "apple " ,"orange " , "limon"
basket = x + y + z
print(basket)
