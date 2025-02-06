Pattern Printing
Right Triangle Star Pattern
Printing star patterns is a common exercise to practice looping in Python. Here are some simple star patterns you can print:
Right Triangle Star Pattern:
Print a right-angled triangle of stars.
def right_triangle(rows):
    for i in range(1, rows + 1):
        print("*" * i)

right_triangle(5)
# Output:
# *
# **
# ***
# ****
# *****


Pyramid Star Pattern:
Print a pyramid of stars.
def pyramid(rows):
    for i in range(1, rows + 1):
        spaces = " " * (rows - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

pyramid(5)
# Output:
#     *
#    ***
#   *****
#  *******
# *********


Hollow Square Star Pattern:
Print a hollow square of stars.
def hollow_square(rows):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * rows)
        else:
            print("*" + " " * (rows - 2) + "*")

hollow_square(5)
# Output:
# *****
# *   *
# *   *
# *   *
# *****