n, m = [int(i) for i in input().split()]
a, res, diff = [], [], abs(n - m)
for t in range(n):
    a += [[int(i) for i in input().split()]]
if n >= m:
    for i in range(n):
        if not (not i % 2 and i/2 < diff):
            res += [a[i]]
    for i in range(m):
        print(*res[i])
else:
    for j in range(m):
        if not (j % 2 and (j-1)/2 < diff):
            res += [[a[i][j] for i in range(n)]]
    for j in range(n):
        for i in range(n):
            print(res[i][j], end=' ')
        print()