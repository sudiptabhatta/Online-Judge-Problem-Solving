'''
given a list of names print the names that exists more than once
input = ['paul', 'sudipta', 'paul', 'abc', 'cde', 'abc']
output = ['paul', 'abc']

'''

array = ['paul', 'sudipta', 'paul', 'abc', 'cde', 'abc']
found = []
unique = []
length = len(array) # 6

for i in range(0, length):
    for j in range(0, length):
        if j != i and array[i] == array[j]:
            found.append(array[i])
            break

# print(found)

for number in found:
    if number not in unique:
        unique.append(number)

print(unique)









