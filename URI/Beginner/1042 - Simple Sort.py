numbers = input().split()

x, y, z = numbers

ascending_list = [int(x), int(y), int(z)]
ascending_list.sort()

for item in ascending_list:
    print(f'{item}')
print('')

for item in numbers:
    print(f'{item}')


