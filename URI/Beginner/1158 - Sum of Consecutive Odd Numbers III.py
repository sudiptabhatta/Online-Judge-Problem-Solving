N = int(input())

for i in range(N):
    X, Y = list(map(int, input().split()))
    sum = 0
    if X % 2 == 0:
        X = X + 1
    for i in range(Y):
        sum = sum + X
        X += 2
    print(sum)













        