# mySet = {1,"Hello",2.0,(1,2,3)}

# #this set consists of list as its element, which is a mutable type hence it can't be an element in the list, (nor does lists, set itself or dictionaries)
# mySet2 = {1,3,"Hello",[1,2,3]}

# for j in mySet2:
#     print(j)

# for i in mySet:
#     print(i)

# emptySet = {}

# print(emptySet)


# fruits = {"banana","apple","kiwi"}
# print(fruits)
# fruits.add("guava")
# print(fruits)

# fruits.remove("banana")
# fruits.discard("banana")
# print(fruits)

# fruits = {"banana","apple","kiwi"}
# print(fruits.pop())

# emptySet = {}
# print(emptySet.pop())


#joining two sets

set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}
set4 = {8,9,0}

result = set1 | set2 #union operator

result2 = set1.union(set2) #union method
result3 = set1.union(set2, set3, set4)#multiple sets

print(result3)

#using the update method, which will change the first set itself without returning a new set
set1.update(set2, set3)
print(set1)

x = {3,4}
y = {3,4,5,6}
x.intersection_update(y)
print(x)

newResult = x.intersection(y)
print(newResult)

print(x.isdisjoint(y))
print(x.issubset(y))