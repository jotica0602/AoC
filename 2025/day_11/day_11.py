import os
from collections import deque
from functools import cache
with open(f'{os.path.dirname(__file__)}/input.txt') as file:
    lines = [line.strip().replace(':','').split() for line in file.readlines()]

G = {line[0]:set(line[1:]) for line in lines}
G['out'] = {}

def bfs(start):
    q = [start]
    paths = 0
    while q:
        v = q.pop(0)
        for n in G[v]:
            if n == 'out': paths += 1
            q.append(n)
    return paths

@cache
def dfs(start,count):
    if start == 'out' and count == 2:
        return 1
    if start == 'out':
        return 0
    
    paths = 0
    for n in G[start]:
        paths += dfs(n, count + 1 if n == 'dac' or n == 'fft' else count)
    return paths

def solve(part):
    ans = 0
    if part == 1:
        ans = bfs(start='you')
    if part == 2:
        ans = dfs('svr',0)
    return ans

print(solve(part=1))
print(solve(part=2))