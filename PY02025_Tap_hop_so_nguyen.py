n, m = [int(i) for i in input().split()]
a = {int(i) for i in input().split()}
b = {int(i) for i in input().split()}
print(*a&b)
print(*a^(a&b))
print(*b^(a&b))