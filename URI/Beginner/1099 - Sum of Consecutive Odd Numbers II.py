N = int(input())

for i in range(N):
    X, Y = list(map(int, input().split()))
    sum = 0
    if X == Y:
        print(0)
    else:
        if X > Y:
            temp = X
            X = Y
            Y = temp
        j = X + 1
        while j < Y:
            if j % 2 != 0:
                sum = sum + j
            j += 1
        print(sum)

                