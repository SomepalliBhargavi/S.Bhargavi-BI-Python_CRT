Set1={1,2,3}
Set2={3,4,5}
#intersection()
Set1.intersection(Set2)
print(Set1.intersection(Set2))

#union()
Set1.union(Set2)
print(Set1.union(Set2))

#difference()
Set1.difference(Set2)
print(Set1.difference(Set2))

#issubset()
Set_a={4,6,8}
Set_b={2,4,6,8,10,12,14,16,18}
print(Set_a.issubset(Set_b))
print(Set_b.issubset(Set_a))
#issuperset()
print(Set_a.issuperset(Set_b))
print(Set_b.issuperset(Set_a))