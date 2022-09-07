for t in range(int(input())):
    n, res = int(input()), 0
    a = [int(i) for i in input().split()]
    for i in range(n-1):
        s = set()
        for j in range(i+1, n):
            tmp = -(a[i] + a[j])
            if tmp in s:    res += 1
            else:           s.add(a[j])
    print(res)