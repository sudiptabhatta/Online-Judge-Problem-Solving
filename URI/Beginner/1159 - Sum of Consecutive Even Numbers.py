while True:
    sum = 0
    N = int(input())
    if N == 0:
        break
    if N % 2 != 0:
        N += 1
    for i in range(5):
        sum = sum + N
        N = N + 2
    print(sum)

