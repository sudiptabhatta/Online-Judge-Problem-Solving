N = int(input())
i = 0

while i < N:
    number = int(input())
    sum = 0
    for j in range(1, number):
        if number % j == 0:
            sum = sum + j
    if sum == number:
        print(f'{number} eh perfeito')
    else:
        print(f'{number} nao eh perfeito')
    i += 1