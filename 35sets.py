#sets are defined using curly braces `{}` or by using the `set()` constructor.
#Creating a Set:
#Using curly braces 
my_set = {1, 2, 3, 4, 5}
#Using the set() constructor
another_set = set([5, 6, 7, 8, 9])

#Adding Elements to a Set:
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
#Removing Elements from a Set:
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}
#Remove an element without raising an error if the element is not present
my_set.discard(10)
#Pop removes and returns an arbitrary element from the set
popped_element = my_set.pop()
print(popped_element, my_set)  # Output (random order): 1, {2, 4, 5}