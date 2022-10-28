N = int(input())

for number in range(1, N+1):
    if number % 2 == 0:
        even_square = number ** 2
        print(f'{number}^2 = {even_square}')