Built-in Functions
max() and min() - Returns the maximum and minimum values from a sequence.
numbers = [10, 5, 8, 15, 3]
max_value = max(numbers)
min_value = min(numbers)
print(max_value)  # Output: 15
print(min_value)  # Output: 3


sum() - Returns the sum of elements in a sequence.
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print(total_sum)  # Output: 15


range() - Generates a sequence of numbers within a specified range.
# Generate numbers from 0 to 4
my_range = range(5)
print(list(my_range))  # Output: [0, 1, 2, 3, 4]


sorted() - Returns a new sorted list from the elements in an iterable.
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]