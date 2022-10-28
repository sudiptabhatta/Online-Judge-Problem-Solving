while True:
    num_pairs = input().split()
    X, Y = num_pairs
    X = int(X)
    Y = int(Y)
    if X == Y:
        break
    else:
        if X < Y:
            print('Crescente')
        else:
            print('Decrescente')