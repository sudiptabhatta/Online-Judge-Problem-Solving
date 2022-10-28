X = float(input())
N = [X]
print('N[0] = %.4f'%N[0])
i = 1

while i < 100:
    N.append((N[i - 1]) / 2)
    print(f'N[{i}] = %.4f'%N[i])
    i += 1
