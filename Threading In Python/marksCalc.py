from functools import reduce

marks = [34,38,23,40,23,17,34,36,37,29]

total = reduce(lambda x, y: x + y, marks)
average = total/10

print("The average marks is: ", average)