#Function Arguments

#Positional Arguments:
#Positional arguments are the most basic type of arguments. They are matched to function parameters based on their order of appearance.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

#Calling the function with positional arguments
greet("kesava", 21)  # Output: Hello, kesava You are 21 years old.

#Keyword Arguments:
#Keyword arguments are specified with the parameter name followed by the value, separated by an equal sign.
#These arguments allow you to pass the values to the function in any order.

def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with keyword arguments in a different order
greet(age=21, name="Bavisetti")  # Output: Hello, Bavisetti You are 21 years old.

#Default Values:
#You can provide default values for function parameters. 
#If a value is not passed for that parameter when the function is called, the default value will be used.
def greet(name, age=21):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function without specifying 'age' argument
greet("kesava")  # Output: Hello, kesava You are 21 years old.

# Calling the function with 'age' argument
greet("kesava", 21)  # Output: Hello, kesava You are 21 years old.