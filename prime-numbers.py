'''

Print prime number between specific range. input range will 1 & 30.

'''


# If a number has only two factors 1 and itself, then the number is prime. Also, the number can not be divided by the numbers between 1 and itself so remainder is not zero. 

for number in range(1, 30):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            print(number)



        

        




