N = int(input())

for i in range(N):
    test_cases = input().split()
    num1, num2, num3 = test_cases
    weighted_avg = (2 * float(num1) + 3 * float(num2) + 5 * float(num3)) / (2 + 3 + 5)
    print('%.1f'%weighted_avg)
   