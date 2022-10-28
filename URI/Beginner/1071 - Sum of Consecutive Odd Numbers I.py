X = int(input())
Y = int(input())

sum = 0
i = X - 1

while i > Y:
    if i % 2 != 0:
        sum = sum + i 
    i = i - 1
print(sum)


