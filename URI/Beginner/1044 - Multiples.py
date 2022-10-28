values = input().split()

A, B = values

if (int(A) % int(B) == 0) and (int(B) % int(A) == 0):
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')