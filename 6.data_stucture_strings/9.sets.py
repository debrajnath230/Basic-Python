# Type of collections
# unordered
# unique elements

set1 ={1,2,3,4,5,1}
print(set1)
set1.add(6)
print(set1)
set1.remove(1)
print(set1)
print( 2 in set1)
print( 9 in set1)
set2={1,2,3}
print(set1 & set2)
set1.union(set2)
print(set2.issubset(set1))
print(set1.intersection(set2))
print(set1-set2)