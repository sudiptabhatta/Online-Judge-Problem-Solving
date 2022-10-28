N = int(input())
i = 0

while i < N:
    numbers = input().split()
    X, Y = numbers
    X = int(X)
    Y = int(Y)
    if Y == 0:
        print('divisao impossivel')
    else:
        result = X / Y
        print('%.1f'%result)
    i = i + 1