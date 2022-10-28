age = int(input())

years = age // 365
rem = age % 365  
months = rem // 30
days = rem % 30

print(f'{years} ano(s)')
print(f'{months} mes(es)')
print(f'{days} dia(s)')