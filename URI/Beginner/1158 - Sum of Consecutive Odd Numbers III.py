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




# another approach 
n = int(input())
i = 0

while i < n:
    x, y = list(map(int, input().split()))
    sum = 0

    count = 0
    while count < y:
        if x % 2 != 0:
            sum = sum + x
            count += 1
        x += 1
    i += 1
    print(sum)













        