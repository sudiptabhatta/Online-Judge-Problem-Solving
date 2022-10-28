T = int(input())
temp = 0


for i in range(1000):
    print(f'N[{i}] = {temp}')
    temp += 1
    if temp == T:
        temp = 0

