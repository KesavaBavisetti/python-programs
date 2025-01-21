#stores (collection of items)
#we can't modify (add / remove new data)
#tuples items are represented in parentheses () seperated by comma ,

#Example: Creating a tuple
fruits = ("apple", "banana", "orange")
coordinates = (3.14, 2.71)

#Accessing Elements:

# Example: Accessing elements in a tuple
fruits = ("apple", "banana", "orange")
print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "orange"

#Tuple Packing and Unpacking:

#Example: Tuple packing and unpacking
person = ("John", 30, "New York")
name, age, city = person
print(name)  # Output: "John"
print(age)   # Output: 30
print(city)  # Output: "New York"

#Tuple Functions:
#Tuples support various built-in functions like `len()`, `min()`, and `max()`.
# Example: Tuple functions
numbers = (5, 2, 8, 1, 7)

# Length of the tuple
length = len(numbers)
print(length)  # Output: 5

# Maximum and minimum elements in the tuple
maximum = max(numbers)
minimum = min(numbers)
print(maximum, minimum)  # Output: 8 1


#Tuple Concatenation and Repetition:

#Example: Tuple concatenation and repetition
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

#Concatenation
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)

#Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)