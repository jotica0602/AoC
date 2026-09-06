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

seeds = [(seeds[i],seeds[i] + seeds[i+1] - 1) for i in range(0,len(seeds),2)]
p2 = float('inf')
for s in seeds:
    S = [s]
    for m in maps:
        next = []
        while S:
            s,e = S.pop()
            for i in range(len(maps[m])):
                c,a,b = maps[m][i]
                os = max(s,a)
                oe = min(e, a + b - 1)
                overlaps = os < oe
                if overlaps:
                    next.append(((os - a) + c, (oe - a) + c - 1))
                    if s < os:
                        S.append((s, os - 1))
                    if e > oe:
                        S.append((oe + 1, e))
                    break
            if not overlaps:
                next.append((s,e))

            
        S = next
    p2 = min(p2,min(S)[0])
print(p2)
