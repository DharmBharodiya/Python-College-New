def count_till(n):
    count = 1
    while count <= n:
        # return count # this won't work over here
        yield count #instead we'll have to use yield whenever an iterable needs to be returned
        count += 1

for count in count_till(5):
    print(count)

# def countTill(n):
#     count = 1
#     while count <= n:
#         count+=1
#         # return count # this won't work over here
#         return count #instead we'll have to use yield whenever an iterable needs to be returned
       

# for count in count_till(5):
#     print(count)

