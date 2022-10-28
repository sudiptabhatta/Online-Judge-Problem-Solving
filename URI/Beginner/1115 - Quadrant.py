while True:
    coordinates = input().split()
    X, Y = coordinates
    X = int(X)
    Y = int(Y)
    if X == 0 or Y == 0:
        break
    else:
        if X > 0 and Y > 0:
            print('primeiro')
        elif X < 0 and Y < 0:
            print('terceiro')
        elif X > 0 and Y < 0:
            print('quarto')
        elif X < 0 and Y > 0:
            print('segundo')
        