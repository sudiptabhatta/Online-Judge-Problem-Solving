values = input().split()

x, y = values

if float(x) > 0 and float(y) > 0:
    print('Q1')
elif float(x) < 0 and float(y) < 0:
    print('Q3')
elif float(x) > 0 and float(y) < 0:
    print('Q4')
elif float(x) < 0 and float(y) > 0:
    print('Q2')
elif float(x) == 0 and float(y) == 0:
    print('Origem')
elif float(y) == 0:
    print('Eixo X')
elif float(x) == 0:
    print('Eixo Y')