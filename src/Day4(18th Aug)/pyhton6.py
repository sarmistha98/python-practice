#python string formatting (f-string)
name='cathy'
country='UK'
print("cathy is from UK") # this is manually print
print(f'{name} is from {country}') # this is dynamically print

#Identation(dynamic string)...> when you use the "for" loop
lst=['abc','fgh']
lst1=[1]
for val in lst:
    for val1 in lst1:
        print(f'for {val} in lst {val1} is assinged from lst1')