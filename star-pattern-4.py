'''

A 
B B 
C C C 
D D D D 
E E E E E

'''

arr = ['A', 'B', 'C', 'D', 'E']

for i in range(1, 6):
    for j in range(1, i + 1):
        print(arr[i-1], end=' ')

    print()