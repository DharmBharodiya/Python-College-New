theList = [1,2,3,4,5,6]
emptyList = []
# for x in theList:
#     print(x)

print("Checking empty list.")

#empty list evaluates `False`, and if so the not operator will make it `True` so it will pass the if statement
#hence, the `not` operator can be used to check empty container
# if not emptyList:
#     print("The list is empty.2")
# else:
#     print("The list is not empty.2")

# if len(emptyList) == 0:
#     print("The list is empty.2")
# else:
#     print("The list is not empty.2")

if emptyList == []:
    print("The list is empty. 3")
else:
    print("The list is not empty.3")