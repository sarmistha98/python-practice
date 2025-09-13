#frozenset :- it returns a unchangable frozenset() object which like set only but not changleable .
#It will not allow indexing also as its unorder
x=[1,2,3,4,10,11, 12]
frozen_set=frozenset(x)
print(x)
print(type(x))
print(frozen_set)
print(type(frozen_set))

#we can not add, update or remove operation on fronzenset beacuse they are immutable
#we can do only normal set operation like:- copy,differenec,union,intersection

