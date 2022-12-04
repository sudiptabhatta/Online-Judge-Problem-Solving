'''
input matrix:

1 2 3
4 5 6 
7 8 9
10 11 12

output matrix:

1 2 3
6 5 4 
7 8 9
12 11 10

'''


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
row_length = len(matrix)

for row in range(row_length):
    
    col_length = len(matrix[row])
    if row % 2 != 0:
        for col in range(col_length-1, -1, -1):
            print(matrix[row][col], end=' ')
    else:
        for col in range(col_length):
            print(matrix[row][col], end=' ')
    print('')





