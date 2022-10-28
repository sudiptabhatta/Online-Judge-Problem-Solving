N = int(input())

numbers = []

for i in range(N):
    number = int(input())
    numbers.append(number)
    
for number in numbers:
    if number % 2 == 0:
        if number > 0:
            print('EVEN POSITIVE')
        elif number < 0:
            print('EVEN NEGATIVE')
        else:
            print('NULL')
    elif number % 2 != 0:
        if number > 0:
            print('ODD POSITIVE')
        elif number < 0:
            print('ODD NEGATIVE')
        else:
            print('NULL')