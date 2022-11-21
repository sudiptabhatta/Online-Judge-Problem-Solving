'''
Check if a Number is a Palindrome 


number = 1221

1221 // 10 = 122 -> number
1221 % 10 = 1 -> rem
rev = 0 * 10 + 1 = 1


122 // 10 = 12 -> number
122 % 10 = 2 -> rem
rev = 1 * 10 + 2 = 12

12 // 10 = 1 -> number
12 % 10 = 2 -> rem
rev = 12 * 10 + 2 = 122


1 // 10 = 0 -> number
1 % 10 = 1 -> rem
rev = 122 * 10 + 1 = 1221



'''

number = 1221
temp = number
rev = 0

while number > 0:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10

if rev == temp:
    print('palindrome')
else:
    print('not palindrome')


'''

print palindrome numbers between 1 to 30.


'''
for number in range(1, 30):
    temp = number
    rev = 0
    while number > 0:
        rem = number % 10
        rev = rev * 10 + rem
        number = number // 10

    if rev == temp:
        print(temp)



