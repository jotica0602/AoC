from heapq import heappop, heappush

dirs = {'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)} 

def opposite(dir):
        if dir == 'N': return 'S'
        elif dir == 'S': return 'N'
        elif dir == 'E': return 'W'
        else: return 'E'
        
def is_valid(x,y,grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
def relax(x,y,direction,score,scores,grid,q):
    if is_valid(x,y,grid) and grid[x][y] != '#' and scores[(x,y,opposite(direction))] > score: 
        scores[(x,y,opposite(direction))] = score
        heappush(q,(score,x,y,direction))
        
def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j],sep='',end='')
        print()


class day_16:
    def solve_part1(self):
        with open('input.txt','r') as file:
            grid = [list(line) for line in file.read().split('\n')]
            
        sx,sy,ex,ey = self.get_start_and_end(grid)
        scores = self.dijkstra(grid,sx,sy,'E')
        
        ans = float('inf')
        for d in ['N','S','E','W']:
            ans = min(ans,scores[(ex,ey,d)])
            
        return ans
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            grid = [list(line) for line in file.read().split('\n')]
        
        sx,sy,ex,ey = self.get_start_and_end(grid)
        d1 = self.dijkstra(grid,sx,sy,'E')
        
        best_dir = 'E'
        for d in dirs:
            if d1[(ex,ey,d)] < d1[(ex,ey,best_dir)]:
                best_dir = d
        
        best = d1[(ex,ey,best_dir)]
        d2 = self.dijkstra(grid,ex,ey,best_dir)
        
        tiles = set()
        
        ans = 0
        for x,y,d in d1:
            # print((x,y),d1[(x,y,d)],d2[(x,y,d)],d1[(x,y,d)]+d2[(x,y,d)], d1[(x,y,d)]+d2[(x,y,d)] == best)
            if d1[(x,y,d)] + d2[(x,y,opposite(d))] == best:
                # ans += 1
                tiles.add((x,y))
                grid[x][y] = 'O'
        
        # print_grid(grid)
        return len(tiles) + 1
    
    def get_start_and_end(self,grid):
        s = (-1,-1)
        fpos = (-1,-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'S':
                    sx,sy = (i,j)
                if grid[i][j] == 'E':
                    ex,ey = (i,j)
        return sx,sy,ex,ey
    
    def dijkstra(self,grid,sx,sy,sd):
        scores = {(i,j,d):float('inf') for i in range(len(grid)) for j in range(len(grid[0])) for d in dirs if grid[i][j] != '#'}
        scores[(sx,sy,sd)] = 0
        q = [(0,sx,sy,sd)]
        
        while q:
            current_score,vx,vy,dir = heappop(q)
            if current_score > scores[(vx,vy,dir)]: continue
            for d in dirs:
                if dir != d:
                    relax(vx,vy,d,current_score + 1000,scores,grid,q)
                else: 
                    dx,dy = dirs[d][0],dirs[d][1]
                    nx,ny = vx + dx, vy + dy
                    relax(nx,ny,d,current_score + 1,scores,grid,q)
        
        return scores
        
        
solver = day_16()
print(solver.solve_part1())
print(solver.solve_part2())