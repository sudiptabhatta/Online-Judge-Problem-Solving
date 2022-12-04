'''

Given an n x n array. print the sum of each column.
1 2 3
4 5 6
7 8 9


'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
length = len(matrix)


for col in range(length):
    sum = 0
    for row in range(length):
        sum = sum + matrix[row][col]
    print(f'sum of {col} number column = {sum}')

