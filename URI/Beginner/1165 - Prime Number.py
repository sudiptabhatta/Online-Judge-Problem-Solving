N = int(input())
i = 0

while i < N:
    X = int(input())
    count = 0
    for j in range(1, X + 1):
        if X % j == 0:
            count = count + 1
    if count == 2:
        print(f'{X} eh primo')
    else:
        print(f'{X} nao eh primo')
    i += 1