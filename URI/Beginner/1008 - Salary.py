employee_number = int(input())
worked_hours_per_month = int(input())
amount_per_hour = float(input())

salary = worked_hours_per_month * amount_per_hour
print(f'NUMBER = {employee_number}')
print('SALARY = U$ %.2f'%salary)
