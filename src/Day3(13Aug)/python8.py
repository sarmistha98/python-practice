#Nested tuple
x=('Tee',(0,5),('Tee','maya'),(3.4,'pi','go'),'Tee')
print(x)
print(x[1][0])
print(x[2][1])

#count
print(x.count('Tee'))
#delete:- you can not delete the element in tuple as its immutable but you can delet the whole tuple

#single element declared in tuple (to identify the tuple, you give comma)
l1=[1]
l2=(1)
t1=(1,)
print(type(t1))
print(type(l1))
print(type(l2))



