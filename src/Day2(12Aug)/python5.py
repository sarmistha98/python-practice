#while loop

number=1
while number<=3:
    print(number)
    number=number+1

#print the number until the user enter 0

number=int(input("Enter a number: "))
while number!=0:
    print(f'you enter {number} ')
    number=int(input("Enter a number: "))
print("The end.")
