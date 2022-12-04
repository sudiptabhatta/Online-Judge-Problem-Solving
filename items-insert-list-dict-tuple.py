'''

input = [1, 2, 4, 5]

The task is to insert the list of numbers into the dictionary first where the numbers of that list will be the keys in the 
dictionary and corresponding values of those keys will be the converted words. Then add those values to a tuple.

output: ('one', 'two', 'four', 'five')

'''


arr = [1, 2, 4, 5]
dict = {} # empty dictionary


for i in arr:
    if i == 1:
        dict[i] =  'one'
    elif i == 2:
        dict[i] =  'two'
    elif i == 4:
        dict[i] = 'four'
    elif i == 5:
        dict[i] = 'five'

# print(dict)


# tup = tuple(dict.keys())
tup = tuple(dict.values()) 
print(tup)