N = int(input())
i = 0
coelhos = 0
ratos = 0
sapos = 0

while i < 10:
    test_cases = input().split()
    amount, animal_type = test_cases
    amount = int(amount)
    if animal_type == 'C':
        coelhos += amount
    elif animal_type == 'R':
        ratos += amount
    elif animal_type == 'S':
        sapos += amount
    i += 1
    
sum = coelhos + ratos + sapos
c = (coelhos / sum) * 100
r = (ratos / sum) * 100
s =  (sapos / sum) * 100

print(f'Total: {sum} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print('Percentual de coelhos: %.2f %%' %c)
print('Percentual de ratos: %.2f %%' %r)
print('Percentual de sapos: %.2f %%' %s)
