#string method is used for many cases they are 
#1)len(): its used for lenght of string
str = "Kesava Bavisetti"
len = len(str)
print(len)

#2)lower(): it converts all characters in the string to lower case
str = "KESAVA BAVISETTI"
lower_case = str.lower()
print(lower_case)

#3)upper(): it converts all characters in the string to upper case 
str = "Kesava Bavisetti"
upper_case = str.upper()
print(upper_case)

#4)strip(): it removes leading & trailing (front & back) whitespaces from the string
str = "      Kesava Bavisetti     "
stripped_str = str.strip()
print(stripped_str)

#5)replace(): its occurrences of a substring  with another substring (new string)
str = "Kesava Bavisetti"
new_str = str.replace("Kesava","Sainath")
print(new_str)

#6)split(): it splits the string into a list of substrings based on a delimiter (list)
str = "mango, apple, orange"
fruits = str.split(",")
print(fruits)

#7)startswith(): it checks if the str starts with a specific perfix (true or false)
str = "Kesava Bavisetti"
result = str.startswith("Kesava")
print(result)

#8)endswith(): it checks if the str ends with a specific suffix (true or false)
str = "Kesava Bavisetti"
result = str.endswith("Bavisetti")
print(result)

#9)count(): Returns the number of occurrences of a substing in the string (repeated alphabets)
str = "Kesava Bavisetti"
count = str.count("i")
print(count)

#10)find(): returns the index of the first occurrence  of a substring . if not found returns -1 (position)
str = "Kesava Bavisetti"
index = str.find("B")
print(index)

#11)isdigit(): checks if all characters in the string are digits
str = "4578"
result = str.isdigit()
print(result)

#11)isalpha(): checks if all characters in the string are alphabetic
str = "Kesava"
result = str.isalpha()
print(result)