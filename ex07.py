n, k, m = input().split()
if int(k) < int(m):
    print(int(m)-1 - int(k))
else:
    print(int(n)-int(k) + int(m)-1)
