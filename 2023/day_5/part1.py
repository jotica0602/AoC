import re
from collections import defaultdict

sp = r'seeds: ((?:\d+\s)+)'
mp = r'map:\s((?:\d+\s)+)'
with open('input.txt') as f:
    lines = f.read()

seeds = list(map(int,re.findall(sp,lines)[0].strip().split()))
mps = [l.strip().split('\n') for l in re.findall(mp,lines)]
maps = defaultdict(list[list[int]])

for m in range(len(mps)):
    for i in range(len(mps[m])):
        maps[m].append(list(map(int,mps[m][i].split())))

p1 = float('inf')
for seed in seeds:
    x = seed
    for m in maps:
        for i in range(len(maps[m])):
            c,a,b = maps[m][i]
            if a <= x <= (a + b) - 1:
                x = (x - a) + c
                break
    p1 = min(p1,x)
print(p1)
