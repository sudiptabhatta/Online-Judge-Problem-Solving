seller_name = input()
fixed_salary = float(input())
value = float(input())

total_sold_percent = value * 0.15
total = fixed_salary + total_sold_percent
print('TOTAL = R$ %.2f'%total)
