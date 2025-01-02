#if , elseif(elif) , else these 3 are conditional statements in python
#used for true or false 
#condition 1) if block is true it will execute otherwise 
#condition 2) elif block will execute , (if & elif) both statements are false then
#condition 3) else block will execute

#example for if statement
age = 7
if age < 18:
    print("u r a minor")
elif age >= 18:
    print("u r an adult")
else:
    print("u r an senior citizen")

#example for elif statement
age = 18
if age < 18:
    print("u r a minor")
elif age >= 18:
    print("u r an adult")
else:
    print("u r an senior citizen")

#example for else statement
age = 45
if age < 18:
    print("u r a minor")
elif age >= 55:
    print("u r an adult")
else:
    print("u r an senior citizen")
