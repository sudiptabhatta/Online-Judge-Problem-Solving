while True:
    X = float(input())
    sum = 0
    count = 0

    while count < 2:
        if X >= 0 and X <= 10:
            sum = sum + X 
            count = count + 1 
        else:
            print('nota invalida')
    
    print("media = %.2f" % (sum / 2.0))
    print('novo calculo (1-sim 2-nao)')

    while True:
        t = int(input())
        print('novo calculo (1-sim 2-nao)')
        if t == 1:
            break
    if X == 2:
        break 
