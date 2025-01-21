#stores (collection of items)
#we can modify (add new data)
#list items are represented in square brackets [] seperated by comma ,

#Examples
#Creating a list of numbers
numbers = [1, 2, 3, 4, 5]

#Creating a list of strings
fruits = ["apple", "banana", "orange"]

# Creating a mixed-type list
mixed_list = [1, "apple", True, 3.14]

#Accessing Elements

#Example: Accessing elements in a list
fruits = ["apple", "banana", "orange"]

print(fruits[0])  # Output: "apple"
print(fruits[2])  # Output: "orange"

#Modifying Elements

#Examples
# Modifying elements in a list
fruits = ["apple", "banana", "orange"]
fruits[1] = "grape"
print(fruits)  # Output: ['apple', 'grape', 'orange']

#List Operations
#Example: List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

#Concatenation
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]

# Repetition
repeated_list = list1 * 3
print(repeated_list)  # Output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

#List Methods:-
#Example: List methods
fruits = ["apple", "banana", "orange"]

#Adding elements
fruits.append("grape")
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

#Removing elements
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'orange', 'grape']

#Sorting elements
fruits.sort()
print(fruits)  # Output: ['apple', 'grape', 'orange']