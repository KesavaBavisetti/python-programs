#nested conditional statements(cs) mainly used for complex (in&out) conditions like
#nested if,elif & else blocks are present in both inside & outside of the statement 
#if block(in &out) or elif block(in&out) both statements correct it will execute otherwise
#else block (in&out) will execute

#nested if example
x = 8
if x > 0: #inside
    print("x is positive!")
    if x % 2 == 0: #outside
        print("x is even number!")
    else: #inside
        print("x is not positive!")
else: #outside
        print("x is odd number!")

#nested elif example
marks = 86
if marks >= 90: #inside
    print("Grade A!")
elif marks >= 75: #inside
    print("Grade B!")
    if marks >= 85: #outside
            print("Excellent!")
elif marks >= 75: #outside
        print("Good!")
else:
    print("Grade below C!")
