#its used to repeatedly execute a block of code as long as specifed code is true , until the statement becomes false 
num = 1
while num <= 7:
    print (num)
    num += 1
    #it will print 1 to 7 numbers & exit after 7 num bcz condition becomes false 

#another example

num = 3
sum_of_numbers = 0

while num <= 10:
    sum_of_numbers += num
    num +=1
    print("sum_of _numbers from 1 to 10:", sum_of_numbers) #total52
#its first adds 0+3=3 , 3+4=7 , 7+5=12 , 12+6=18 , 18+7=25 , 25+8=33 , 33+9=42 , 42+10=52  after 10 it will exit bcz condition becomes false 

