import re
from sys import stdin

res = ''
inputString = stdin.readlines()
for line in inputString:
    res += re.sub('[\.\?\!]+', '\n',' '.join(re.split('\\s+', line.strip().lower())))
for i in (re.split('\n\s?', res)):
    if i != '':
        print(i[0:1].upper() + i[1:])