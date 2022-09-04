s1 = input().split()
s2 = input()
index = int(input()) - 1
s1[index] = s2 + s1[index]
print(*s1)