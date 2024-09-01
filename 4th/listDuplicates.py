theList = [1,2,2,3,4,5,5,6,7,7,7,8]

newList = list(set(theList))

#set does not allow duplicate elements, hence we converted our list to set first and then back to list in order to remove all the duplicate elements from it
print("List before: ", theList)
print("List after: ", newList)