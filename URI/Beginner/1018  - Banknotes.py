value = int(input())

a = value // 100 
# print(a)
rem = value % 100
# print(rem)
b = rem // 50
# print(b)
rem = rem % 50
# print(rem)
c = rem // 20 
rem = rem % 20
d = rem // 10
rem = rem % 10
e = rem // 5
rem = rem % 5
f = rem // 2 
rem = rem % 2
g = rem // 1
rem = rem % 1

print(f'{value}')
print(f'{a} nota(s) de R$ 100,00')
print(f'{b} nota(s) de R$ 50,00')
print(f'{c} nota(s) de R$ 20,00')
print(f'{d} nota(s) de R$ 10,00')
print(f'{e} nota(s) de R$ 5,00')
print(f'{f} nota(s) de R$ 2,00')
print(f'{g} nota(s) de R$ 1,00')
