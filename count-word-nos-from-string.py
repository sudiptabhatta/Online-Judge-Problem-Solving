'''

Count number of word from a string
example:
input: beautiful bangladesh
output: 2

'''

str = 'beautiful bangladesh'
words = []
temp = ''

for i in str:
    if i == ' ':
        words.append(temp)
        temp = ''
    else:
        temp = temp + i

if len(temp) > 0:
    words.append(temp)

print(len(words))
# print(words)






