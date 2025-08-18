#dict can not have duplicate keys. it will override the duplicate
d={'name':'maya','age':32,'name':'tee','name':'sarm'}
print(d)

#add new keys:values pair
d={'name':'maya','age':32,'name':'tee','name1':'misty'}
print(d)

#dict can have duplicate values
f={'name':'maya','age':32,'name':'tee','name1':'maya'}
print(f)

#convert list to dict : using zip()
x=['tee',20]
y=['jagan',100]
p=dict(zip(x,y))
print(p)