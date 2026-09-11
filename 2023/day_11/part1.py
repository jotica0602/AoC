import os
with open(os.path.abspath(__file__).removesuffix('part1.py')+'input.txt') as file:
    lines = file.read().split()
grid = [[*line] for line in lines]
n,m = len(grid), len(grid[0])
nr = []
for i in range(n):
    if '#' not in grid[i]:
        nr.append(i)

nc = []
for i in range(m):
    exists = False
    for j in range(n):
        if grid[j][i] == '#':
            exists = True
    if not exists:
        nc.append(i)

galaxies = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '#':
            galaxies.append((i,j))

def expand(x,nr,nc,factor):
    x1,x2 = x
    x1 += len([r for r in nr if r < x1]) * (factor - 1)
    x2 += len([c for c in nc if c < x2]) * (factor - 1)
    return (x1,x2)

def md(x1,x2,y1,y2):
    return abs(x1-y1) + abs(x2-y2)

ans = 0
for i in range(len(galaxies)-1):
    x1,x2 = expand(galaxies[i],nr,nc,2)
    for j in range(i+1,len(galaxies)):
        y1,y2 = expand(galaxies[j],nr,nc,2)
        ans += md(x1,x2,y1,y2)
print(ans)