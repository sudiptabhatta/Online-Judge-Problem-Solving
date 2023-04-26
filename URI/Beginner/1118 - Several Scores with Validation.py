while True:
    sum = 0
    i = 0
    while i < 2:
        X = float(input())
        if (X >= 0 and X <= 10):
            sum += X
            i += 1
        else:
            print("nota invalida")
    print("media = %.2f" % (sum / 2))
    t = 0
    while True:
        print("novo calculo (1-sim 2-nao)")
        t = int(input())
        if t == 1 or t== 2:
            break
    if t == 2:
        break