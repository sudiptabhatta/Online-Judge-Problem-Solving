'''

Given an n x n array. print the sum of each row.
1 2 3
4 5 6
7 8 9


'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
length = len(matrix)

for row in range(length):
    sum = 0
    for col in range(length):
        sum = sum + matrix[row][col]
    print(f'sum of {row} number row = {sum}')



# another approach
for row in matrix:
    sum = 0
    for col in row:
        sum = sum + col
    print(f'sum of {row} row = {sum}')