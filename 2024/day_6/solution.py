import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j],sep=' ',end='')
        print(end='\n')
    
class day6:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        map = [list(line) for line in text.splitlines()]
        visited = [[False for _ in row] for row in map]
        
        guard_pos = self.find_guard(map)
        guard = Guard(guard_pos,map)
        
        while True:
            visited[guard.x][guard.y] = True
            dx = guard.direction[guard.dir][0]
            dy = guard.direction[guard.dir][1]
            if guard.is_out_of_bounds(guard.x + dx, guard.y + dy,map):
                break
            else:
                guard.move(dx,dy,map)
            
        ans = 0
        
        for i in range(len(visited)):
            for j in range(len(visited[i])):
                if visited[i][j]:
                    ans += 1
                    
                    
        return ans
    
    def find_guard(self, map):
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == '^':
                    guard_pos = (i,j)
                    break
                
        return guard_pos
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        map = [list(line) for line in text.splitlines()]
        visited = [[False for _ in row] for row in map]
        guard_initial_pos = self.find_guard(map)
        ans = 0
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] != '.':
                    continue
                map[i][j] = '#'
                ans += detect_loop(guard_initial_pos, map, visited)
                map[i][j] = '.'
                
        return ans                    
        
    
class Guard:
    def __init__(self,guard_pos,map) -> None:
        self.x = guard_pos[0]
        self.y = guard_pos[1]
        self.direction = [(-1,0),(0,1),(1,0),(0,-1)]
        self.dir = 0
        self.char = '^'
        
    def is_out_of_bounds(self,x,y,map):
        return x < 0 or x == len(map) or y < 0 or y == len(map)
            
    def rotate(self,map):
        self.dir = (self.dir + 1) % 4
        
        # if self.dir == 0:
        #     self.char = '^'
        #     map[self.x][self.y] = self.char
        # elif self.dir == 1:
        #     self.char = '>'
        #     map[self.x][self.y] = self.char
        # elif self.dir == 2:
        #     self.char = 'v'
        #     map[self.x][self.y] = self.char
        # else:
        #     self.char = '<'
        #     map[self.x][self.y] = self.char
            
    def move(self,dx,dy,map):
        if map[self.x + dx][self.y + dy] == '#':
            self.rotate(map)
            return
        
        # map[self.x][self.y] = '.'
        
        self.x = self.x + dx
        self.y = self.y + dy
        
        # map[self.x][self.y] = self.char
        
def detect_loop(guard_initial_pos,map,visited):
    guard = Guard(guard_initial_pos, map)
    visited = set()
    # clean_map(map)
    # map[guard.x][guard.y] = '^'
    
    while True:
            dx = guard.direction[guard.dir][0]
            dy = guard.direction[guard.dir][1]
            visited.add((guard.x,guard.y,dx,dy))
            if guard.is_out_of_bounds(guard.x + dx, guard.y + dy,map):
                return 0
            else:
                guard.move(dx,dy,map)
            if (guard.x,guard.y,guard.direction[guard.dir][0],guard.direction[guard.dir][1]) in visited:
                return 1
            
def clean_map(map):
    for i in range(len(map)):
        for j in range(len(map)):
            if map[i][j] == '^' or map [i][j] == '>' or map[i][j] == 'v' or map[i][j] == '<':
                map[i][j] = '.'
    

solver = day6()
print(solver.solve_part1())
print(solver.solve_part2())