def solution():
    s = input()
    a = dict()
    result = ''
    for i in range(0,len(s), 2):
        a[s[i]] = int(s[i+1])
    for char in a.keys():
        for cou in range(a[char]):
            result += char
    print(result)
for t in range(int(input())):
    solution()
