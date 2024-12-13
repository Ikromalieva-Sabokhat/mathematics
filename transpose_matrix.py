#8.1
def transpose_matrix(matrix):
    transposed_matrix=[]
    for i in range(len(matrix[0])): #3
        new_line = []
        for j in range(len(matrix)):#4
            new_line.append(matrix[j][i])
        transposed_matrix.append(new_line)
    return transposed_matrix
print(transpose_matrix([[1,2,3,2],[4,5,6, 3],[7,3,8,9]]))