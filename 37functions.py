#Creating a Function:
#To define a function, you use the `def` keyword, followed by the function name, a pair of parentheses `()`, and a colon `:`. 
#The code block inside the function is indented and contains the instructions that the function will execute when called.

def greet():
    print("Kesava Bavisetti!")
# Calling the function
greet()  # Output: Kesava Bavisetti

#Function Parameters:
#You can define parameters inside the parentheses to pass data into the function. 
#Parameters act as placeholders for the actual values that you provide when calling the function.

def greet_user(name):
    print(f"Kesava, {name}!")
# Calling the function with an argument
greet_user("Bavisetti")  # Output: Kesava Bavisetti


#Return Statement:
#Functions can return values using the `return` keyword. When a function returns a value, you can capture it and use it elsewhere in your code.

def add_numbers(a, b):
    return a + b

#Calling the function and storing the result in a variable
result = add_numbers(3, 5)
print(result)  # Output: 8