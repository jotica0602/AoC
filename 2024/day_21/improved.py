from itertools import product
import re

def neighbors(vx,vy):
    pos = [(0,-1,'<'),(0,1,'>'),(-1,0,'^'),(1,0,'v')]
    for x,y,d in pos:
        yield vx + x, vy + y,d
    
def is_valid(x,y,grid):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

def dfs(grid,x,y):
        distances = {grid[i][j]:float('inf') for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != '*'}
        distances[grid[x][y]] = 1
        moves = {grid[i][j]: [] for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] != '*'}
        moves[grid[x][y]] = 1
        dfs_visit(x,y,grid,distances,moves,'',1)
        # for key in moves:
        #     minlen = min(map(len,moves[key]))
        #     moves[key] = set(move for move in moves[key] if len(move) == minlen)
        return moves
            
def dfs_visit(vx,vy,grid,distances,moves,path,actual):
    for nx,ny,move in neighbors(vx,vy):
        if not is_valid(nx,ny,grid): continue
        if grid[nx][ny] == '*': continue
        if distances[grid[nx][ny]] < actual + 1: continue

        distances[grid[nx][ny]] = actual + 1 
        moves[grid[nx][ny]] = actual + 1
        dfs_visit(nx,ny,grid,distances,moves,path + move, actual + 1)
        
def get_min_len(seqs):
    return min(list(map(len,seqs)))

def get_moves(from_,to,message,moves):
    if message in moves[from_]:
        return moves[from_][message]
    
    if len(message) == 1:
        return moves[from_][to]
    
    seqs = get_moves(message[0],message[1],message[1:],moves)
    m = [a + b for a,b in product(moves[from_][to],seqs)]
    minlen = get_min_len(m)
    m = [seq for seq in m if len(seq) == minlen]
    moves[from_][message] = m
    return m


def get_next_seq(seqs,moves):
    nextseq = []
    for seq in seqs:
        nextseq += get_moves('A',seq[0],seq,moves)
    minlen = get_min_len(nextseq)
    nextseq = [seq for seq in nextseq if len(seq) == minlen]
    return nextseq
    
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
        
        kbmoves = {kb[i][j]: dfs(kb,i,j) for i in range(len(kb)) for j in range(len(kb[0])) if kb[i][j] != '*'}
        ctmoves = {controller[i][j]: dfs(controller,i,j) for i in range(len(controller)) for j in range(len(controller[0])) if controller[i][j] != '*'}

        # It can be improved using memoization
        ans = 0
        
        for message in messages:
            seqs = get_next_seq([message],kbmoves)
            for i in range(2):
                si = get_next_seq(seqs,ctmoves)
                seqs = si
            
            ans += get_min_len(seqs) * int(re.findall(r'\d+',message)[0])
        return ans
    
    def solve_part2(self):
        pass
    

solver = day21()
print(solver.solve_part1())
print(solver.solve_part2())