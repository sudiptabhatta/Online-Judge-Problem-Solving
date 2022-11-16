# print starts in this format

'''  

* 
* * 
* * * 
* * * * 
* * * * *

'''


for i in range(1, 6): # outer loop for number of rows
    for j in range(1, i + 1): # inner loop for number of columns
        print('*', end=' ')
    
    print() 


print('-----------------')

# another approach
for i in range(1, 6):
    for j in range(1, i + 1):
        if j == i:
            print('*')
        else:
            print('*', end=' ')









 
