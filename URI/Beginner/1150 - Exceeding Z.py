X = int(input())

while True:
    Z = int(input())
    if Z > X:
        break

sum = X
count = 1

while sum < Z:
    sum = sum + X + count
    count = count + 1

print(count)