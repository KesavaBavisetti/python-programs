#it coverts one data type into another data type by using built in fun
#int() to float() to str() etc
#int to str
num_int  = 57
#57 is int
print(type(num_int))
num_string = str (num_int)
#coverting int into str
print(num_string)
#now 57 is converted into str
print(type(num_string)) 

#float to integer
num_float = 57.35
print(type(num_float))
#7.35 is float
num_integer = int(num_float)
#converting into int
print(num_int)
print(type(num_int))

#boolean(True or False) to integer
boolean_value = True
#True means any str,numbers (expect0),list 
#False means number 0, none , empty values like( (), {} ,"", [] )
int_value = int(boolean_value)
#coverting bool into int
print(int_value)      
