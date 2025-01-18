#comparing strings in python
#equal & not equalcomparison (==,=!)
string1 = "hello"
string2 = "Hello"
if string1 == string2:
    print("Both strings are equal.")
else:
    print("The strings are not equal.")
if string1 != string2:
    print("The strings are not equal.")
else:
    print("Both strings are equal.")

#example forLexicographical comparison
string1 = "apple"
string2 = "banana"
if string1 < string2:
    print("string1 comes before string2.")
else:
    print("string1 comes after or is equal to string2.")
if string1 <= string2:
    print("string1 comes before or is equal to string2.")
else:
    print("string1 comes after string2.")
if string1 > string2:
    print("string1 comes after string2.")
else:
    print("string1 comes before or is equal to string2.")
if string1 >= string2:
    print("string1 comes after or is equal to string2.")
else:
    print("string1 comes before string2.")

