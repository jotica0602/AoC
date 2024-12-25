import regex
import os
import time as t
import keyboard

class Robot:
    def __init__(self,px,py,vx,vy) -> None:
        self.py,self.px = int(px),int(py)
        self.vy,self.vx = int(vx),int(vy)
        
    def __repr__(self) -> str:
        return f'pos: {self.px,self.py} vel: {self.vx,self.vy}'
    
class day14:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        pattern = r'p=(\d+),(\d+)\sv=(-?\d+),(\-?\d+)'
        matches = regex.findall(pattern,text)
        n,m = 103, 101
        time = 100
        robots = []
        
        for i in range(len(matches)):
            px,py,vx,vy = matches[i]
            robots.append(Robot(px,py,vx,vy))
        
        for i in range(len(robots)):
            for j in range(time):
                robot:Robot = robots[i]
                robot.px = (robot.px + robot.vx) % n
                robot.py = (robot.py + robot.vy) % m
        
        c1,c2,c3,c4 = 0,0,0,0
        for robot in robots:
            if robot.px < n//2 and robot.py > m//2:
                c1 += 1
            if robot.px < n//2 and robot.py < m//2:
                c2 += 1
            if robot.px > n//2 and robot.py < m//2:
                c3 += 1
            if robot.px > n//2 and robot.py > m//2:    
                c4 += 1
            
        return c1*c2*c3*c4
    
    def find_neighbors(self,x,y,cc,repr,grid):
        positions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        for i,j in positions:
            if self.is_valid(x+i,y+j,grid) and grid[x+i][y+j] > 0 and (x+i,y+j) not in cc[repr]:
                cc[repr].append((x+i,y+j))
                self.find_neighbors(x+i,y+j,cc,repr,grid)
    
    def is_valid(self,x,y,grid):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def print_grid(self,grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    print('*',sep='',end='')
                else:
                    print('.',sep='',end='')
            print()
            
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        pattern = r'p=(\d+),(\d+)\sv=(-?\d+),(\-?\d+)'
        matches = regex.findall(pattern,text)
        n,m = 103, 101
        robots = []
        grid = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(len(matches)):
            px,py,vx,vy = matches[i]
            robots.append(Robot(px,py,vx,vy))
        
        for i in range(len(robots)):
            robot:Robot = robots[i]
            grid[robot.px][robot.py] += 1
            
        c = 0
        while True:
            print("\033c", end="")  
            for i in range(len(robots)):
                robot = robots[i]
                grid[robot.px][robot.py] -= 1  
                robot.px = (robot.px + robot.vx) % n  
                robot.py = (robot.py + robot.vy) % m
                grid[robot.px][robot.py] += 1  
            c += 1
            ccs = {}
            lcc = -1
                
            for i in range(n):
                for j in range(m):
                    if grid[i][j] > 0:
                        if (i,j) not in ccs:
                            ccs[(i,j)] = [(i,j)]
                        self.find_neighbors(i,j,ccs,(i,j),grid)

            for cc in ccs:
                lcc = max(len(ccs[cc]),lcc) 
                # print(lcc)
                
            if lcc >= 229:
                self.print_grid(grid)
                print(lcc)
                print(c)
                t.sleep(5)
                return c
        
solver = day14()
print(solver.solve_part1())
print(solver.solve_part2())