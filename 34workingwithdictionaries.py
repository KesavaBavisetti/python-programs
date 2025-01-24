#Modifying and Adding Key-Value Pairs:
#Example: Modifying and adding key-value pairs
student = {
    "name": "Kesava Bavisetti",
    "age": 21,
    "major": "Electronics & communication",
    "gpa": 8.7
}

#Modifying value
student["gpa"] = 9.0
#Adding new key-value pair
student["university"] = "JNTUK"
print(student)
#Output: {'name': 'Kesava Bavisetti', 'age': 21, 'major': 'Electronics & communication', 'gpa': 9.0, 'university': 'JNTUK'}


#Dictionary Methods:
#Python provides various built-in methods to perform common operations on dictionaries.
#Example: Dictionary methods
student = {
    "name": "Kesava Bavisetti",
    "age": 21,
    "major": "Electronics & communication",
    "gpa": 8.7
}
#Get keys and values
keys = student.keys()
values = student.values()
print(keys)   # Output: dict_keys(['name', 'age', 'major', 'gpa'])
print(values) # Output: dict_values(['Kesava Bavisetti', 21, 'Electronics & communication', 8.7])

#Check if a key exists in the dictionary
if "major" in student:
    print("Major:", student["major"])  # Output: Major: Electronics & communication

#Remove a key-value pair from the dictionary
removed_value = student.pop("age")
print("Removed Value:", removed_value)  # Output: Removed Value: 21
print(student)  # Output: {'name': 'Kesava Bavisetti', 'major': 'Electronics & communication', 'gpa': 8.7}