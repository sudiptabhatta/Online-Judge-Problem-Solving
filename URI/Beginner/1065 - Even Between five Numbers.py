count = 0

for i in range(5):
    number = input()
    if int(number) % 2 == 0:
        count += 1
print(f'{count} valores pares')