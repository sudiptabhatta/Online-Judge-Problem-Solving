numbers = input().split()

# A, B, C = numbers
A = float(numbers[0])
B = float(numbers[1])
C = float(numbers[2])

if (A + B > C) and (A + C > B) and (B + C > A):
    Perimetro = A + B + C
    print('Perimetro = %.1f'%Perimetro) 
else:
    Area = 0.5 * (A + B) * C
    print('Area = %.1f'%Area) 