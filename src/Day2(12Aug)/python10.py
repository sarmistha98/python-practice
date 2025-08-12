# continue statement
#continue with for loop
for i in range(5):
    if i==3:
        continue
    print(i)

#continue with while loop
#WAP to print the odd number from 1 to 10
num=0
while num<10:
    num+=1
    if (num%2)==0:
        continue
    print(num)