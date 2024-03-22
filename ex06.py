n = int(input())
m = int(input())
k = int(input())
if n == m == k:
    print(3)
elif n == m or n == k or m == k:
    print(2)
else:
    print(1)
