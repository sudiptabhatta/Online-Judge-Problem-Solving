'''
given a string reverse it without using built-in function
input = paul out = luap

'''

str = 'paul'
arr = []

for i in str:
    arr.append(i)


j = 0

while j < 2:
    temp = arr[j]
    arr[j] = arr[-(j+1)] 
    arr[-(j+1)] = temp
    j += 1

for k in arr:
    print(k, end='')



