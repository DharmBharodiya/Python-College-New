def theGenerator(num):
    count = 1
    while(count <= num):
        yield count
        count += 1

genIterator = theGenerator(5)

for num in genIterator:
    print(num)


# print(next(genIterator))
# print(next(genIterator))
# print(next(genIterator))