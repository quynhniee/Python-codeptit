a, n = [], int(input())
for i in range(n):
    a += [input()]
s = a[0]
ok, ans = 1, int(1e9)
for i in range(len(s)):
    d = 0
    for j in range(n):
        x = a[j]
        for k in range(len(s)):
            if x == s:
                d += k
                break
            x = x[1:] + x[0]
        if x != s:  ok = 0
    ans = min(ans, d)
    s = s[1:] + s[0]
print(-1 if not ok else ans)

