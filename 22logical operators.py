#these are 3 types in python
#if x and y are operands 
#1) and :- it returns both operands x and y are true 
#2) or :- it returns atleast one operands either x or y are true 
#3) not :- it returns opposite boolean value of the operand (true = false)

#and both operators are true 

x = 5
y = 7
z = (x<7) and (y>5)
print(z) #true

x = 5
y = 7
z = (x>7) and (y>5)
print(z) #false

#or atleast one operand is true 
x = 5
y = 7
z = (x<7) or (y<5)
print(z) #true

x = 5
y = 7
z = (x>7) or (y<5)
print(z) #false

#not means if operand is true it returns false 

x = 5
y = 7
z = not (x>y)
print(z) #true

x = 5
y = 7
z = not (x<y)
print(z) #false