n, m, k = input().split()
if n >= m and n > k and m >= k:
    print(n, m, k)
elif n >= k and n > m and k >= m:
    print(n, k, m)
elif m >= n and m > k and n >= k:
    print(m, n, k)
elif m >= k and m > n and k >= n:
    print(m, k, n)
elif k >= m and k > n and m >= n:
    print(k, m, n)
else:
    print(k, n, m)
