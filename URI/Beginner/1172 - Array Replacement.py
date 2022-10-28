i = 0
X = []

while i < 10:
    N = int(input())
    if N <= 0:
        X.append(1)
        print(f'X[{i}] = {X[i]}')
    else:
        X.append(N)
        print(f'X[{i}] = {X[i]}')
    i = i + 1

# print(X)



    
