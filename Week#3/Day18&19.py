"""----------Day18&19---------"""
#Exercise1
List1 = [ 'A' , 'B' , 'C' , 'D' , 'E' ]
List1.append('F')
print(List1)
List1.remove('A')
print(List1)
List1.reverse()
print(List1)
List2 = List1.copy()
print(List2)

#Exercise2
tuple1 = ('java', 'python', 'swift')
if 'python' not in tuple1:
    print("No, it's not in tuple1")
if 'python' in tuple1:
    print("Yes, it's in tuple1")
