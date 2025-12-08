from functools import cache
with open('input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]
    n,m = len(grid), len(grid[0])

def solve(part):
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
        ans = bfs(sx,sy)
    if part == 2:
        ans = dp(sx,sy)
        # ans = dfs(sx,sy)
    return ans

def is_valid(x,y):
    n,m = len(grid),len(grid[0])
    return 0 <= x < n and 0 <= y < m

def add(x:int, y:int, visited:set,q:list[int]):
    if is_valid(x,y) and (x,y) not in visited:
        visited.add((x,y))
        q.append((x,y))

def bfs(sx,sy):
    q = [(sx,sy)]
    ans = 0
    visited = set()
    ans = 0
    while q:
        vx,vy = q.pop(0)
        if grid[vx][vy] == 'S' or grid[vx][vy] == '.':
            add(vx+1,vy,visited,q)
        if grid[vx][vy] == '^':
            ans += 1
            add(vx,vy-1,visited,q)
            add(vx,vy+1,visited,q)
    return ans

# full dp solution
def dp(x,y):
    dp = [[0] * m for _ in range(n)]
    dp[x][y] = 1
    for i in range(n):
        for j in range(m):
            if is_valid(i+1,j) and grid[i+1][j] == '.':
                dp[i+1][j] += dp[i][j]
            if is_valid(i+1,j) and grid[i+1][j] == '^' and is_valid(i+1,j-1):
                dp[i+1][j-1] += dp[i][j]
            if is_valid(i+1,j) and grid[i+1][j] == '^' and is_valid(i+1,j+1):
                dp[i+1][j+1] += dp[i][j]
    return sum(dp[n-1])

# recursive + memo
@cache
def dfs(x,y):
    if x == n - 1: 
        return 1
    if grid[x][y] == 'S' or grid[x][y] == '.' and is_valid(x+1,y):
        return dfs(x+1,y)
    if grid[x][y] == '^':
        l = 0
        r = 0
        if is_valid(x,y-1):
            l = dfs(x,y-1)
        if is_valid(x,y+1):
            r = dfs(x,y+1)
        return l + r

print(solve(part=1))
print(solve(part=2))