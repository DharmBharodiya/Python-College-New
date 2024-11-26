set1 = {1,2,3,4}

#the elements of the set needs to be only of the immutable type, hence lists, sets, dictionaties or any other mutable type of data cannot be the element of a set


set2 = {1,2,3,4,4,5}
#printing this set would only print {1,2,3,4,5} as set doesn't allow duplicates so 4 would be implicitly removed
print(set2)

#nor will it print 4 for two times over here
for i in set2:
    print(i)

#the set() method can also be used to create sets in python
theList = [1,2,3,4,4,5]
setFromList = set(theList)#duplicates 4 will be removed and it'll only appear for one time
print(setFromList)

#you can also create empty set in python
emptySet = {}

#accessing the set items
#sets are unordered and unindexed and hence we can only access its elements by iterating over the whole set, and being unordered everytime you try to access it the results could come up differently than then previous time
set3 = {4,5,6,"hello","world",5.9,(1,23,5)}
for i in set3:
    print(i, end=" | ")

print()
#adding items to the set
set4 = {6,7,8,9}
set4.add(10)
print(set4)

#removing items from the set
set4.remove(7)
print(set4)

# discard() method can also be used instead of the remove one, the only difference is that the `discard` method doesn't raise any exception if the element to be removed is not available in the set, while the remove() method does
set4.discard(6)

#popping element form the set
#this will return the element that will be removed from the set
set5 = {3,5,6,7,34}
poppedElement = set5.pop()
print("Popped Element: ", poppedElement)

#clear() method empties the whole set
set6 = {4,5,6,7}
print("Set 6 :", set6)
set6.clear()
print("Set 6 : ",set6)

#the del keyword deletes the set completely
set7 = {1,23,4}
print("Set 7 : ", set7)
del set7
#printing this would raise an exception
# print("Set 6 : ", set7)

#joining two sets

#union() method
# -> this methods returns a "whole new set" which is made out of the combination of all the sets mentioned which needs to be combined
unionSet = set1.union(set2)
print(unionSet)

#in the union method, the elements that appear in both/or multiple sets will be added once as set is strict about duplication of elements in it

#update() method
# -> this method doesn't return a whole new set, instead it just "updates the first set" by adding the elements from the other sets to the first one
set1.update(set2)
print(set1)

#union operator ( | )
# -> works same as the union() method but its just that this is an operator 

unionOperatorSet = set1 | set2
print(unionOperatorSet)

# you can also combine muliple sets together with the same methods and operators

set1.update(set2, set3, set4)
print(set1)

#intersection -> which means to have only those elements which appears in all the sets, i.e., basically the set of duplicate elements

#intersection_update() -> this method updates the first set according to the other sets by keeping only the duplicate elements in it
set1.intersection_update(set2)
print(set1)

# intersection() -> this method returns a new set made out of only the duplicate elements from the mentioned sets
intersectedSet = set1.intersection(set2, set3)
print(intersectedSet)

#keep all, but remove the elements
# symmetric_difference_update() -> this method keeps only those element which are not same in the sets mentioned, and updates the first set accordingly
set8 = {1,2,3,4,5}
set9 = {3,4,5,6,7}

set8.symmetric_difference_update(set9)
print(set8)

# symmetric_difference() -> this method returns a new set made out of only non-duplicate elements

# isdisjoint() method -> it returns whether the two sets have intersection or not
# basically it returns "TRUE" if there are no duplicate elements in the given sets

set10 = {11,12,14,15}
set11 = {1,2,4,67}

isIt = set10.isdisjoint(set11)
print("Disjoint: ", isIt)

# issubset() -> returns if a set is a part of the other set or not
set12 = {1,2,3,4,5}
set13 = {2,3,4}

isItSubset = set13.issubset(set12)
print("Subset: ", isItSubset)

# issuperset() -> same as subset one but just for the subset
isItSuperSet = set12.issuperset(set13)
print("Superset: ", isItSuperSet)