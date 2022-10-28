product1 = input().split()
product2 = input().split()

# taking multiple input from user and split them
# 15 2 67.5
# ['15', '2', '67.5']
# print(product1)
# print(type(product1)) # list 

prod1_number, prod1_no_unit, prod1_price_one_unit = product1
# print(prod1_number, prod1_no_unit, prod1_price_one_unit)
# print(type(prod1_number), type(prod1_no_unit), type(prod1_price_one_unit))
prod2_number, prod2_no_unit, prod2_price_one_unit = product2
# print(prod2_number, prod2_no_unit, prod2_price_one_unit = product2)
# print(type(prod2_number), type(prod2_no_unit), type(prod2_price_one_unit))


value_to_pay = int(prod1_no_unit) * float(prod1_price_one_unit) + int(prod2_no_unit) * float(prod2_price_one_unit)
print('VALOR A PAGAR: R$ %.2f'%value_to_pay)