i = 0
N = []

while i < 20:
    number = int(input())
    N.append(number)
    i +=1
    
    
j = 0

while j < 10:
    temp = N[j]
    N[j] = N[-(j+1)]
    N[-(j+1)] = temp
    j += 1
    
    
k = 0

while k < 20:
    print(f'N[{k}] = {N[k]}')
    k += 1