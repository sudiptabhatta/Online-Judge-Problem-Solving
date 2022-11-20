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
            



# another approach 
while True:
    values = input().split()
    m, n = values
    i = int(m)
    j = int(n)
    sum = 0
    if i <= 0 or j <= 0:
        break
    else:
        if i > j:
            temp = i
            i = j
            j = temp
        for num in range(i, j+1):
            sum = sum + num
            print(num, end=' ')
        print(f'Sum={sum}')