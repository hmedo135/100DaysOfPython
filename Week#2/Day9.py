"""----------Day9----------"""
#it will replace "age" with {}
age = 23
A = "My name is Abdulhameed , and I'm {} years old"
print(A.format(age))
# if there multi {} we must put numbers inside {}
state = "connect"
service = "stc"
speed = 3.0
B = """My phone number from {2},
it can be {0} to the internet,
and it's speed {1} Mb/s"""
# must words be in orders 2, 0, 1
print(B.format(state, speed, service))
