i = 0
even_count = 0
odd_count = 0
pos_count = 0
neg_count = 0
numbers = []

while i < 5:
    number = int(input())
    numbers.append(number)
    i = i + 1

for number in numbers:
    if number % 2 == 0:
        even_count += 1
    if number % 2 != 0:
        odd_count += 1
    if number > 0:
        pos_count += 1
    if number < 0:
        neg_count += 1


print(f'{even_count} valor(es) par(es)')
print(f'{odd_count} valor(es) impar(es)')
print(f'{pos_count} valor(es) positivo(s)')
print(f'{neg_count} valor(es) negativo(s)')
