def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in row] for row in matrix]

    # Iterate through the elements of the matrix and calculate the square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
