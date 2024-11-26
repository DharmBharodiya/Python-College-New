def matrix_addition(matrix1, matrix2): 
    result = [] 
    # Check if matrices have the same dimensions 
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]): 
        print("Matrices have different dimensions. Addition not possible.") 
        return None 
 
    # Perform matrix addition 
    for i in range(len(matrix1)): 
        row = [] 
        for j in range(len(matrix1[0])): 
            row.append(matrix1[i][j] + matrix2[i][j]) 
        result.append(row) 
    return result 
 
def matrix_multiplication(matrix1, matrix2): 
    result = [] 
    # Check if matrices can be multiplied 
 
    if len(matrix1[0]) != len(matrix2): 
        print("Matrices cannot be multiplied. Incorrect dimensions.") 
        return None 
# Perform matrix multiplication 
    for i in range(len(matrix1)): 
        row = [] 
        for j in range(len(matrix2[0])): 
            sum_element = 0 
            for k in range(len(matrix2)): 
                sum_element += matrix1[i][k] * matrix2[k][j] 
            row.append(sum_element) 
        result.append(row) 
    return result 
 
# Example usage for matrix addition 
matrix_A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
matrix_B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]] 
 
result_addition = matrix_addition(matrix_A, matrix_B) 
print("Matrix Addition Result:") 
for row in result_addition: 
    print(row) 
 
result_multiplication = matrix_multiplication(matrix_A, matrix_B) 
print("Matrix Multiplication Result:") 
for row in result_multiplication: 
    print(row) 