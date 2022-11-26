import math

def isLucky(n, min, max):
    return n == max-min

n, m = [int(i) for i in input().split()]
a, max, min, res = [], -1e6, 1e6, -1
for i in range(n):
    a += [[int(j) for j in input().split()]]
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
        if a[i][j] < min:
            min = a[i][j]
for i in range(n):
    for j in range(m):
        if isLucky(a[i][j], min, max):
            res = a[i][j]
if res == -1:    print('NOT FOUND')
else:
    print(res)
    for i in range(n):
        for j in range(m):
            if a[i][j] == res:
                print(f'Vi tri [{i}][{j}]')