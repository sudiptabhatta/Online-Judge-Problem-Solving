first = 0
second = 1
fib_arr = [first, second]

for i in range(2, 61):
    next = first + second
    fib_arr.append(next)
    first = second
    second = next

N = int(input())

for i in range(N):
    num = int(input())
    print(f'Fib({num}) = {fib_arr[num]}')






