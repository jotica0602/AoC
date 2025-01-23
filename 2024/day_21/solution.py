from itertools import product

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
            moves[key] = list(move for move in moves[key] if len(move) == minlen)
        return moves
            
def dfs_visit(vx,vy,grid,distances,moves,path,actual):
    for nx,ny,move in neighbors(vx,vy):
        if not is_valid(nx,ny,grid): continue
        if grid[nx][ny] == '*': continue
        if distances[grid[nx][ny]] < actual + 1: continue

        distances[grid[nx][ny]] = actual + 1 
        moves[grid[nx][ny]].append(path + move + 'A')
        dfs_visit(nx,ny,grid,distances,moves,path + move, actual + 1)
        
      
def get_seqs(message,kpmoves):
    x = message[0]
    y = message[1]
    
    seqs = kpmoves[x][y]
    message = message[1:]
    for i in range(len(message)-1):
        x = message[i]
        y = message[i+1]
        seqs = [s1+s2 for s1,s2 in product(seqs,kpmoves[x][y])]
    return seqs

def get_min_len(x,y,dpmoves,cache,depth=1):
    if (x,y,depth) in cache:
        return cache[(x,y,depth)]

    if depth == 0: 
        return len(dpmoves[x][y][0])
    
    best = float('inf')
    for seq in dpmoves[x][y]:
        length = 0
        for a,b in zip('A'+seq,seq):
            length += get_min_len(a,b,dpmoves,cache,depth-1)
        best = min(length,best)
    
    cache[(x,y,depth)] = best
    return best

class day21:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        messages = text.split('\n')
        keypad = [
                ['7','8','9'],
                ['4','5','6'],
                ['1','2','3'],
                ['*','0','A']
            ]
        dirpad = [
                        ['*','^','A'],
                        ['<','v','>']
                    ]
        
        kpmoves = {keypad[i][j]: dfs(keypad,i,j) for i in range(len(keypad)) for j in range(len(keypad[0])) if keypad[i][j] != '*'}
        dpmoves = {dirpad[i][j]: dfs(dirpad,i,j) for i in range(len(dirpad)) for j in range(len(dirpad[0])) if dirpad[i][j] != '*'}
        cache = {}

        ans = 0
        for message in messages:
            seqs = get_seqs('A' + message,kpmoves)
            minlen = float('inf')
            
            for seq in seqs:
                length = 0
                for x,y in zip('A'+seq,seq):
                    length += get_min_len(x,y,dpmoves,cache)
                minlen = min(minlen,length)
                
            ans += minlen * int(message[:len(message)-1])
                    
        return ans
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        messages = text.split('\n')
        keypad = [
                ['7','8','9'],
                ['4','5','6'],
                ['1','2','3'],
                ['*','0','A']
            ]
        dirpad = [
                        ['*','^','A'],
                        ['<','v','>']
                    ]
        
        kpmoves = {keypad[i][j]: dfs(keypad,i,j) for i in range(len(keypad)) for j in range(len(keypad[0])) if keypad[i][j] != '*'}
        dpmoves = {dirpad[i][j]: dfs(dirpad,i,j) for i in range(len(dirpad)) for j in range(len(dirpad[0])) if dirpad[i][j] != '*'}
        cache = {}

        ans = 0
        for message in messages:
            seqs = get_seqs('A' + message,kpmoves)
            minlen = float('inf')
            
            for seq in seqs:
                length = 0
                for x,y in zip('A'+seq,seq):
                    length += get_min_len(x,y,dpmoves,cache,24)
                minlen = min(minlen,length)
                
            ans += minlen * int(message[:len(message)-1])
                    
        return ans
    

solver = day21()
print(solver.solve_part1())
print(solver.solve_part2())