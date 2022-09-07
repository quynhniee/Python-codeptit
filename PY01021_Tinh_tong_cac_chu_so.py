import re


for t in range(int(input())):
    s = input()
    print(''.join(sorted(re.findall("\D", s))) + str(sum(int(i) for i in re.findall("\d", s))))