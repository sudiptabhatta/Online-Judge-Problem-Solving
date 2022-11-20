N = int(input())

in_count = 0 
out_count = 0
numbers = []

for i in range(N):
    number = int(input())
    numbers.append(number)

# print(numbers) # list of numbers

for number in numbers: 
    if number >= 10 and number <= 20:
        in_count = in_count + 1
    else:
        out_count = out_count + 1
print(f'{in_count} in')
print(f'{out_count} out')



# another approach
N = int(input())

in_count = 0 
out_count = 0

for i in range(N):
    num = int(input())
    if num >= 10 and num <= 20:
        in_count = in_count + 1
    else:
        out_count = out_count + 1

print(f'{in_count} in')
print(f'{out_count} out')