# p = [False]*100000
max_val = 100000
p = [True for i in range(max_val+1)]
def seivePrime ():
    p[0], p[1] = False, False
    i = 2
    while (i*i <= max_val):
        if p[i]:
            for j in range(i*i, max_val + 1, i):
                p[j] = False
        i += 1
            
n, x = map(int, input().strip().split())
seivePrime()
res = [x]
def primeList ():
    cou, i = 0, 0
    while cou < n:
        if p[i]:    
            res.append(i + res[len(res) - 1])
            cou += 1
        i +=1
    for k in res:
        print(k, end=" ")
    print()
primeList()
        
    