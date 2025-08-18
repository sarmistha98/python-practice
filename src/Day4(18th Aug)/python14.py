#convert from list , tuple to dict (combination of list and tuple)
x=['tee',20]
y=('jagan',100)
z=dict(zip(x,y))
print(z)

#get(): it will return only the valuse for the specified key if it available in the dict. it not there then rerurn none
d={'name':'maya','age':32}
print(d.get('name'))
print(d.get('age'))
print(d.get('school'))

#update(): it integrates a dictinory with another dictor iterable keys:values pairs
d.update({'Edition':'java8'})
print(d)

#copy(): it will return the shadow copy of the main dict
d1=d.copy()
print(d1)

#delete: using del() we can delete the elements by using keys
c={'name': 'maya', 'age': 32, 'Edition': 'java8'}
del(c['name'])
del(c['age'])
print(c)
