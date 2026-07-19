#Without duplicates.

my_set ={1,2,3,4,5,5,5,5,5,5}
print(type(my_set))
print(my_set)
print(my_set)

#Set Operations
#1.Union
a={1,2,3,4,5,5,5,5,5,5}
b={10,11,3,2,5}
print(a.union(b))
#2Intersection
print(a.intersection(b))

#Remove
a.remove(2)
print(a)
#Add
a.add(2)
print(a)