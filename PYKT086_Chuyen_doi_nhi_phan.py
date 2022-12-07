from math import log


f = open('DATA.in', 'r')

s = '0123456789ABCDEFG'
for __ in range(int(next(f))):
    n = int(log(int(next(f)), 2))
    num = next(f).strip()[::-1]
    print(*[s[int(num[i:i+n][::-1], 2)] for i in range(0, len(num), n)][::-1], sep='')