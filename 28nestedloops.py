#it is a loop inside another loop
#5x5 rectangular pattern
for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

#triangle pattern
n=5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

#1to9tables in nested loop
for i in range(1,10):
    for j in range (1,11):
        print(i, "*",j, "=", i*j)
    print()

