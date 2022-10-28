import math 

values = input().split()
A, B, C = values

x = (math.pow(float(B), 2) - 4 * float(A) * float(C))


if float(A) == 0 or x < 0:
    print('Impossivel calcular')
else:
    R1 = (-float(B) + math.sqrt(x)) / (2 * float(A))
    R2 = (-float(B) - math.sqrt(x)) / (2 * float(A)) 
    print('R1 = %0.5f'%R1)
    print('R2 = %0.5f'%R2)


