#Write a program to find frequency of elements of list.

ele = [1,2,1,2,4]
count_dict = {}
for e in ele:
   count =  ele.count(e)
   count_dict[str(e)] = count 

print(count_dict)