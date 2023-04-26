A, N = list(map(int, input().split()))
sum = 0 

while N <= 0:
    N = int(input())
else:
    i = 1
    while i <= N:
        sum = sum + A 
        A += 1 
        i += 1
print(sum)

