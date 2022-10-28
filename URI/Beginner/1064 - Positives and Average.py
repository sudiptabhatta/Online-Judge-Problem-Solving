i = 0
count = 0
sum = 0.0

while i < 6:
    value = input()
    if float(value) > 0:
        count = count + 1
        sum = sum + float(value)
    i = i + 1

print(f'{count} valores positivos')
print('%.1f'%(sum / count))