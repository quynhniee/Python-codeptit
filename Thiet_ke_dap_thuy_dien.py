# IR :))

for __ in range(int(input())):
    n = int(input()) # so luong dap
    p = [int(i) for i in input().split()] # vi tri dap thu i
    h = [int(i) for i in input().split()] # chieu cao cua dap thu i
    stack = []
    higher = [] # vi tri dap dau tien ben trai cao hon dap thu i
    for i in range(n):
        while len(stack) > 0 and h[i] >= h[stack[-1]]:
            stack.pop()
        higher.append(0 if not len(stack) else stack[-1])
        stack.append(i)

    v = [0]*n  # the tich lon nhat co the chua den dap thu i
    v[0] = p[0]*h[0]
    for i in range(1, n):
        v[i] = v[higher[i]] + (p[i] - 1 - p[higher[i]]) * h[i] - sum(h[p[higher[i]]+1:p[i]], 0) if higher[i] > 0 else p[i] * h[i] - sum(h[:i])

    for q in range(int(input())):
        k = int(input())
        if k <= v[n-1]:
            res = 0
            while v[res] < k and res < n-1:
                res += 1
            print(res)
        else:   print('Ngap')
