Set={10,20,30,40,50,60,70,80,90,100}
print(Set)
print(type(Set))

#accessing set item using membership operator
print(30 in Set)

#adding items -add()
Set.add(15)
print(Set)

#to add multiple items to a set -update()
Set.update([12,3,11,34,56])
print(Set)

#to remove a specific item from a set -remove()
Set.remove(10)
print(Set)
#removes an item at the begining of the set,no need to give a value - pop()
Set.pop()
print(Set)
#to remove a specific item - discard()
Set.discard(100)
print(Set)
#to remove all the items from the set - clear()
Set.clear()
print(Set)

# returns a set containing all unique items from the both sets - Union() |
Set1={1,2,3}
Set2={3,4,5}
print(Set1|Set2)

#returns a set containing common items between both sets- Intersection() &
Set1={1,2,3}
Set2={1,2,5}
print(Set1&Set2)

#returns a set  containing items that are only in first set and not in second set - Difference(-)
Set1={1,4,3}
Set2={3,4,5}
print(Set1-Set2)

#returns a set containing items that are in either set,but not both - Symmetric Difference(^)
Set1={1,6,3}
Set2={3,4,5}
print(Set1^Set2)