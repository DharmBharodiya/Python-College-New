from functools import reduce
from collections import Counter

# List of numbers
numbers = [1, 2, 3, 2, 1, 2, 4, 4, 4]

# Count occurrences of each number
count_dict = Counter(numbers)

# Find the number with an odd count using reduce and lambda
odd_occurrence_number = reduce(
    lambda x, y: y if count_dict[y] % 2 != 0 else x,
    count_dict,
    None
)

print(f"Number occurring odd number of times: {odd_occurrence_number}")
