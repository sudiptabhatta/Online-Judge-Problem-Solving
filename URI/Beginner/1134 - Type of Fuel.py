alcool_customers = 0
gasolina_customers = 0
diesel_customers = 0

while True:
    fuel_type = int(input())
    if fuel_type == 4:
        break
    else:
        if fuel_type == 1:
            alcool_customers += 1
        elif fuel_type == 2:
            gasolina_customers += 1
        elif fuel_type == 3:
            diesel_customers += 1
        
    
print('MUITO OBRIGADO')
print(f'Alcool: {alcool_customers}')
print(f'Gasolina: {gasolina_customers}')
print(f'Diesel: {diesel_customers}')