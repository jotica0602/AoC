from collections import deque
from functools import cache
import re
import sys

def neighbors(vx,vy):
    pos = [(0,-1,'<'),(0,1,'>'),(-1,0,'^'),(1,0,'v')]
    for x,y,d in pos:
        yield vx + x, vy + y,d
    
def is_valid(x,y,grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def dfs(grid,x,y):
        distances = {grid[i][j]:float('inf') for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != '*'}
        distances[grid[x][y]] = 0
        moves = {grid[i][j]: [] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != '*'}
        moves[grid[x][y]] = ['A']
        dfs_visit(x,y,grid,distances,moves,'',0)
        for key in moves:
            minlen = min(map(len,moves[key]))
            moves[key] = [move for move in moves[key] if len(move) == minlen]
        return moves
            
def dfs_visit(vx,vy,grid,distances,moves,path,actual):
    for nx,ny,move in neighbors(vx,vy):
        if not is_valid(nx,ny,grid): continue
        if grid[nx][ny] == '*': continue
        if distances[grid[nx][ny]] < actual + 1: continue

        distances[grid[nx][ny]] = actual + 1 
        moves[grid[nx][ny]].append(path + move + 'A')
        dfs_visit(nx,ny,grid,distances,moves,path + move, actual + 1)

# @cache
def get_moves(start,message,movesfrom,seq,best,seqs):
    
    if message == '' and len(seq) <= best[0]:
        best[0] = len(seq)
        seqs.append(seq)
        return seq
    
    if len(seq) > best[0]:
        return seq
    
    button = message[0]    
    for s in movesfrom[start][button]:
        r1 = get_moves(button,message[1:],movesfrom,seq + s,best,seqs)
    return r1

class day21:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        messages = text.split('\n')
        kb = [
                ['7','8','9'],
                ['4','5','6'],
                ['1','2','3'],
                ['*','0','A']
            ]
        controller = [
                        ['*','^','A'],
                        ['<','v','>']
                    ]
        
        movesfromkb = {kb[i][j]: dfs(kb,i,j) for i in range(len(kb)) for j in range(len(kb[0])) if kb[i][j] != '*'}
        movesfromct = {controller[i][j]: dfs(controller,i,j) for i in range(len(controller)) for j in range(len(controller[0])) if controller[i][j] != '*'}

        # It can be improved using memoization
        ans = 0
        for message in messages:
            m = sys.maxsize
            seqs = []
            r1 = []
            r2 = []
            get_moves('A',message,movesfromkb,'',[sys.maxsize],seqs)

            for seq in seqs:
                get_moves('A',seq,movesfromct,'',[sys.maxsize],r1)
            for seq in r1:
                get_moves('A',seq,movesfromct,'',[sys.maxsize],r2)

            ans += min(list(map(len,r2))) * int(re.findall(r'\d+',message)[0])
        return ans
    
    def solve_part2(self):
        pass
    

solver = day21()
print(solver.solve_part1())
print(solver.solve_part2())