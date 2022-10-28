salary = float(input())

if salary >= 0 and salary <= 400.00:
    percentage = 15
    money_earned = salary * 0.15
    new_salary = salary + money_earned
    print('Novo salario: %.2f'%new_salary)
    print('Reajuste ganho: %.2f'%money_earned)
    print(f'Em percentual: {percentage} %')
elif salary >= 400.01 and salary <= 800.00:
    percentage = 12
    money_earned = salary * 0.12
    new_salary = salary + money_earned
    print('Novo salario: %.2f'%new_salary)
    print('Reajuste ganho: %.2f'%money_earned)
    print(f'Em percentual: {percentage} %')
elif salary >= 800.01 and salary <= 1200.00:
    percentage = 10
    money_earned = salary * 0.10
    new_salary = salary + money_earned
    print('Novo salario: %.2f'%new_salary)
    print('Reajuste ganho: %.2f'%money_earned)
    print(f'Em percentual: {percentage} %')
elif salary >= 1200.01 and salary <= 2000.00:
    percentage = 7
    money_earned = salary * 0.07
    new_salary = salary + money_earned
    print('Novo salario: %.2f'%new_salary)
    print('Reajuste ganho: %.2f'%money_earned)
    print(f'Em percentual: {percentage} %')
elif salary > 2000.00 :
    percentage = 4
    money_earned = salary * 0.04
    new_salary = salary + money_earned
    print('Novo salario: %.2f'%new_salary)
    print('Reajuste ganho: %.2f'%money_earned)
    print(f'Em percentual: {percentage} %')
    