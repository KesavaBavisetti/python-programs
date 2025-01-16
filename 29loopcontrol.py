#loop control are 3 types they are 
#1)break , 2)continue & 3)pass

#1) break is uesd to stop the loop

for num in range (1,6):
    if num == 3:
        break #it will stop loop before 3
    print(num)

#2) continue is used to skip iteration of a loop & move to next iteration

for num in range(1,6):
    if num % 2 == 0:
        continue #it will skip printing even num (divisible by 2)
    print(num)


#3)pass is used to do nothing inside the loop
for num in range(1,6):
    pass #execute nothing 
