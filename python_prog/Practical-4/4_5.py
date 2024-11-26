n = 5

for i in range(1, n + 1):
    row = [1]
    for j in range(1, i):
        row.append(row[j-1] * (i - j) // j)
    
    spaces = ' ' * (n - i)
    formatted_row = ' '.join(map(str, row))
    print(spaces + formatted_row)