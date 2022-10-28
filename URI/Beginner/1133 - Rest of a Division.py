X = int(input())
Y = int(input())

if X > Y:
    temp = X
    X = Y
    Y = temp

while X < Y:
    X = X + 1
    if X % 5 == 2 or X % 5 == 3 and X != Y:
        print(X)

    
    