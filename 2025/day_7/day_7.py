from functools import cache
with open('input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

def solve(part):
    n,m = len(grid), len(grid[0])
    sx,sy = (0,0)
    found = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx,sy = i,j
                found = True
                break
        if found: break
    
    ans = 0
    if part == 1:
        ans = bfs(sx,sy,n,m)
    if part == 2:
        ans = dfs(sx,sy,n,m)
    return ans

def add(x:int, y:int, visited:set,q:list[int], n:int, m:int):
    if 0 <= x < n and 0 <= y < m and (x,y) not in visited:
        visited.add((x,y))
        q.append((x,y))

def is_valid(x,y,n,m):
    return 0 <= x < n and 0 <= y < m

def bfs(sx,sy,n,m):
    q = [(sx,sy)]
    ans = 0
    visited = set()
    ans = 0
    while q:
        vx,vy = q.pop(0)
        if grid[vx][vy] == 'S' or grid[vx][vy] == '.':
            add(vx+1,vy,visited,q,n,m)
        if grid[vx][vy] == '^':
            ans += 1
            add(vx,vy-1,visited,q,n,m)
            add(vx,vy+1,visited,q,n,m)

    return ans

@cache
def dfs(x,y,n,m):
    if x == n - 1: 
        return 1
    if grid[x][y] == 'S' or grid[x][y] == '.' and is_valid(x+1,y,n,m):
        return dfs(x+1,y,n,m)
    if grid[x][y] == '^':
        l = 0
        r = 0
        if is_valid(x,y-1,n,m):
            l = dfs(x,y-1,n,m)
        if is_valid(x,y+1,n,m):
            r = dfs(x,y+1,n,m)
        return l + r
    

print(solve(part=1))
print(solve(part=2))