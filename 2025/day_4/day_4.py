with open('input.txt') as file:
    grid = [list(line.strip()) for line in file.readlines()]

def solve(grid,part):
    ans = 0
    n = len(grid)
    m = len(grid[0])
    if part == 1:
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@' and count_neighbors(grid,i,j,n,m) < 4:
                    ans += 1
        return ans
    
    if part == 2:
        while True:
            change = False
            to_remove = set()
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == '@' and count_neighbors(grid,i,j,n,m) < 4:
                        ans += 1
                        to_remove.add((i,j))
                        change = True

            for element in to_remove:
                x,y = element
                grid[x][y] = '.'

            to_remove.clear()
            if not change: break
        return ans

def count_neighbors(grid,x,y,n,m):
    neighbors = 0
    for i in range(-1,2):
        for j in range (-1,2):
            if i == 0 and j == 0: continue
            if 0 <= x+i < n and 0 <= y+j < m and grid[x+i][y+j] == '@':
                neighbors += 1
    return neighbors

print(solve(grid,part=1))
print(solve(grid,part=2))