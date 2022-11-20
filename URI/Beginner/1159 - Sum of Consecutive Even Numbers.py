while True:
    sum = 0
    x = int(input())
    if x == 0:
        break
    else:
        for i in range(5):
            if x % 2 == 0:
                sum += x
                i += 1
            x += 1
        print(sum)



# another approach
while True:
    X = int(input())
    sum = 0
    count = 0

    if X == 0:
        break

    while count < 5:
        if X % 2 == 0:
            sum = sum + X
            count = count + 1
        X = X + 1
    print(sum)

