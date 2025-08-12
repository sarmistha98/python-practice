#Nested for loop

attributes=['electronic','fast']
cars=['tesla','marcedies','nano']
for a in attributes:
    for c in cars:
        print(a,c)
    print('------')
print('outside the statement')