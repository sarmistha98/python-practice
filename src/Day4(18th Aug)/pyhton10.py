#Intersection:- it will give the common elements in both sets
t={'hello',1,4,200,10}
t1={'hi',45,67,10,500,10}
inter=t & t1
print(inter)

#union:- it will give all the element without any duplicate
print(t.union(t1))

#issuperset()
print(t.issuperset(t1))
x={"f","e","d","c","d"}
y={"d","c","e"}
print(x.issuperset(y))