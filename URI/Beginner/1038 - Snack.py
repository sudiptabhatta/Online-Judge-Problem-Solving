numbers = input().split()

X, Y = numbers

if int(X) == 1:
    total = int(Y) * 4.00
    print('Total: R$ %.2f'%total)
elif int(X) == 2:
    total = int(Y) * 4.50
    print('Total: R$ %.2f'%total)
elif int(X) == 3:
    total = int(Y) * 5.00
    print('Total: R$ %.2f'%total)
elif int(X) == 4:
    total = int(Y) * 2.00
    print('Total: R$ %.2f'%total)
elif int(X) == 5:
    total = int(Y) * 1.50
    print('Total: R$ %.2f'%total)