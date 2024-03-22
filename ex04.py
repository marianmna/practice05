n = int(input())
if n == 1 or n % 10 == 1 and n != 11:
    print(n, 'попугай')
elif 2 <= n % 10 <= 4 and not 12 <= n <= 14:
    print(n, 'попугая')
else:
    print(n, 'попугаев')
