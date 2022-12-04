'''

Given an n x n array. Write a function to return the diagona sum
1 2 3
4 5 6
7 8 9


'''

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
length = len(matrix)

def diagonalSum(matrix):
    sum = 0
    for row in range(length):
        for col in range(length):
            if row == col:
                sum = sum + matrix[row][col]
    return sum


sum = diagonalSum(matrix)
print(f'Diagonal sum = {sum}')



# another approach without function
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
length = len(matrix)

for row in range(length):
    for col in range(length):
        if row == col:
            sum = sum + matrix[row][col]

print(f'Diagonal sum = {sum}')
    


    


        




