'''

Check if a given string is a Palindrome 

'''

str = 'abbas'
reversed = str[::-1] # the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards

if str == reversed:
    print(f'{str} is a palindrome string')
else:
    print(f'{str} is not a palindrome string')