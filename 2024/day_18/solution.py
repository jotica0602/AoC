import re
import os
from collections import deque
import time

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],sep='',end='')
        print()
        
        
class day18:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        m = re.findall(r'\d+',text)[0:2048]
        bytes = [(int(m[i]),int(m[i+1])) for i in range(0,len(m),2)]
        m,n = 71,71
        
        grid = [['.' for _ in range(n)] for _ in range(m)]
        # print(len(grid),len(grid[0]))
        
        for y,x in bytes:
            # print(f'{x,y} inserted')
            if 0 <= x < m and 0 <= y < n:
                grid[x][y] = '#'
            
        # print_grid(grid)
        d = self.bfs((0,0),m,n,grid)
        # print('end')
        return d[(n-1,n-1)]
    
    def bfs(self,start,m,n,grid):
        visited = {start}
        sx,sy = start
        q = deque([(sx,sy,0)])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        distances = {(i,j): float('inf') for i in range(n) for j in range(n)}

        while q:
            vx,vy,d = q.popleft()
            distances[(vx,vy)] = d
            
            for x,y in dirs:
                nx = vx + x
                ny = vy + y
                 
                if (0 <= nx < m) and (0 <= ny < n) and not (nx,ny) in visited and grid[nx][ny] != '#':
                    q.append((nx,ny,d+1))
                    
            
                visited.add((nx,ny))
        
        return distances
                                    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        m = re.findall(r'\d+',text)
        bytes = [(int(m[i]),int(m[i+1])) for i in range(0,len(m),2)]
        m,n = 71,71
        
        grid = [['.' for _ in range(n)] for _ in range(m)]
        # print(len(grid),len(grid[0]))
        
        
        for i in range(len(bytes)):
            y,x = bytes[i]
            if 0 <= x < n and 0 <= y < n:
                grid[x][y] = '#'
                d = self.bfs((0,0),m,n,grid)
                if d[(n-1,n-1)] == float('inf'):
                    print(i+1 ,(bytes[i][1],bytes[i][0]))
                    return (y,x)
            else:
                continue
        
solver = day18()
print(solver.solve_part1())
print(solver.solve_part2())