from collections import deque
import time

def neighbors(vx,vy):
    pos = [(-1,0),(0,1),(1,0),(0,-1)]
    for x,y in pos:
        yield vx + x, vy + y 

def cheat_neighbors(vx,vy):
    pos = [(0,-2),(1,-1),(2,0),(1,1),(0,2),(-1,1),(-2,0),(-1,-1)]
    for x,y in pos:
        yield vx + x, vy + y 
        
def manhattan_distance(vx,vy,nx,ny):
    return abs(vx - nx) + abs(vy - ny)
        
def bfs(sx,sy,maze,visited):
    d = {(i,j):float('inf') for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] != '#'}
    d[(sx,sy)] = 0
    q = deque([(sx,sy,0)])
    p = {(i,j): None for i in range(len(maze)) for j in range(len(maze[0]))}
    # visited = set()
    
    while q:
        vx,vy,dist = q.popleft()
        visited.add((vx,vy))
        
        for nx,ny in neighbors(vx,vy):
            if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0]) or maze[nx][ny] == '#' or (nx,ny) in visited:
                continue
            d[(nx,ny)] = dist + 1
            p[(nx,ny)] = (vx,vy)
            q.append((nx,ny,dist + 1))
        
    return d
    
class day20:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        maze = [list(i) for i in text.split('\n')]
        sx,sy,ex,ey = self.find_s_and_e(maze)
        
        ds = bfs(sx,sy,maze,set())
        de = bfs(ex,ey,maze,set())
        
        best = ds[(ex,ey)]
        
        ans = 0
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == '#': continue
                for nx,ny in cheat_neighbors(i,j):
                    if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0]): continue
                    if maze[nx][ny] == '#': continue
                    
                    new = ds[(i,j)] + 2 + de[(nx,ny)]
                    if best - new >= 100: 
                        ans += 1                
        return ans
    
    
    def find_s_and_e(self,maze):
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'S':
                    sx,sy = i,j
                if maze[i][j] == 'E' :
                    ex,ey = i,j
        
        return sx,sy,ex,ey

    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        maze = [list(i) for i in text.split('\n')]
        sx,sy,ex,ey = self.find_s_and_e(maze)
        
        visited = set()
        ds = bfs(sx,sy,maze,visited)
        de = bfs(ex,ey,maze,set())
        best = ds[(ex,ey)]
        
        radius = 20        
        ans = 0
        
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == '#': continue
                for nx,ny in visited:
                    md = manhattan_distance(i,j,nx,ny)
                    if md <= 20:
                        new = ds[(i,j)] + md + de[(nx,ny)]
                        if best - new >= 100: 
                            ans += 1                
               
        return ans

    
solver = day20()
print(solver.solve_part1())
print(solver.solve_part2())