A = []

for i in range(100):
    N = float(input())
    A.append(N)
 
i = 0 

while i < 100:
    if A[i] <= 10:
        print(f'A[{i}] = {A[i]}')
    i = i + 1



#another approach
i = 0

while i < 100:
    number = float(input())
    if number <= 10:
        print(f'A[{i}] = {number}')
    i += 1