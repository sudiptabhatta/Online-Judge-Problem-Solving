'''

    * 
   * * 
  * * * 
 * * * * 
* * * * * 


'''

total = 5

for i in range(1, 6):
    num_spaces = total - i
    cur_line = ''

    for j in range(num_spaces):
        cur_line = cur_line + ' '
    cur_line = cur_line + (i * '* ')
    print(cur_line)

