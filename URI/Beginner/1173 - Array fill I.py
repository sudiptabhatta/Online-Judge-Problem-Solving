V = int(input())
i = 1
N = [V]
print(f'N[{0}] = {N[0]}')

while i < 10:
    N.append(2 * N[i - 1])
    print(f'N[{i}] = {N[i]}')
    i = i + 1