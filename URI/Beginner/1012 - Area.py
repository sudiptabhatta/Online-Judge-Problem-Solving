values = input().split()

A, B, C = values
print(type(A))
print('TRIANGULO: %0.3f'%(0.5*float(A)*float(C)))
print('CIRCULO: %0.3f'%(3.14159*float(C)*float(C)))
print('TRAPEZIO: %.3f'%(0.5*(float(A)+float(B))*float(C)))
print('QUADRADO: %0.3f'%(float(B)*float(B)))
print('RETANGULO: %0.3f'%(float(A)*float(B)))