while True:
    values = input().split()
    M, N = values
    i = int(N)
    j = int(M)
    sum = 0
    if i <= 0 or j <= 0:
        break
    else:
        if j > i:
            for i in range(i, j + 1):
                sum = sum + i
                print(i, end=' ')
            print(f'Sum={sum}')
        else:
            for j in range(j, i + 1):
                sum = sum + j
                print(j, end=' ')
            print(f'Sum={sum}')
            