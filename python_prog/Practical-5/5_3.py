str = "hello dev"
dict1= {}
for i in str:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1

print(dict1)