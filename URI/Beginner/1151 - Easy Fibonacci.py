N = int(input())
first = 0
second = 1

if N == 1:
    print(first)
elif(N == 2):
    print(f'{0} {1}')
else:
    print(first, end=' ')
    print(second, end=' ')
    for i in range(N - 2):
        next = first + second
        if i == N - 3:
            print(next)
        else:
            print(next, end=' ')
            first = second
            second = next


 # another approach with list           

# N = int(input())
# fib = [0] * (N+1)
# fib[0] = 0
# fib[1] = 1
# for i in range(2, N+1):
#     fib[i] = fib[i - 1] + fib[i - 2]
    
# for i in range(N):
#     if(i == (N-1)):
#         print(fib[i],end='')
#     else:
#         print(fib[i], end=' ')



