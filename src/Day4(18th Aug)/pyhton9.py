#remove():- to remove th element from the set
y={'hello','python',100,500,2.4}
y.remove('python')
print(y)

#discard():-
y.discard(100)
print(y)

#membership:- in , not in
x={1,2,3,3,5,'tee','python'}
print(3 in x)
print(0 in x)

# print two sets
t={'hello',1,4,200}
t1={'hi',45,67,500}
print(t,t1)
s1=set(['hi',345678,'jhjfjf'])
s2=set([3.4,5678,'maya'])
print(s1,s2)
