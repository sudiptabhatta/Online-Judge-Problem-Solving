numbers = []

for i in range(100):
    number = int(input())
    numbers.append(number)

max = numbers[0]

for number in numbers:
    if number > max:
        max = number
        input_position = numbers.index(max) + 1
print(max)
print(input_position)