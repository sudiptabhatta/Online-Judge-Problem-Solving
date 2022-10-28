N = int(input())

l = list(map(int, input().split())) # map() takes a function object and an iterable as arguments. It returns an iterator that results from applying a transformation function to every item in the original input iterable
positon = 0
min = l[0]
count = 0

for number in l:
    if number < min:
        min = number
        positon = count
    count += 1

print(f'Menor valor: {min}')
print(f'Posicao: {positon}')



