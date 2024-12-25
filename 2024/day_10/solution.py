
class day10:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read().split()
            
        map = [list(line) for line in text]
        n = len(map)
        
        ans = 0
        for i in range(n):
            for j in range(n):
                if map[i][j] == '0':
                    score = [0]
                    nines = set()
                    self.get_trailhead_score(i,j,map,score,nines)
                    ans += score[0]
        return ans
                
    def get_trailhead_score(self,x,y,map,score,nines):
        if not (x,y) in nines and map[x][y] == '9':
            score[0] += 1
            nines.add((x,y))
            return
        
        pos_x = [-1,0,1, 0]
        pos_y = [0, 1,0,-1]
        
        n = len(pos_x)
        height = int(map[x][y])
        for i in range(n):
            newx = x + pos_x[i]
            newy = y + pos_y[i]
            
            if self.is_valid(newx,newy,map) and map[newx][newy].isdigit() and int(map[newx][newy]) == height + 1:
                self.get_trailhead_score(newx,newy,map,score,nines)
                
    def is_valid(self,x,y,map):
        return x >= 0 and x < len(map) and y >= 0 and y < len(map)
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read().split()
            
        map = [list(line) for line in text]
        n = len(map)
        
        ans = 0
        for i in range(n):
            for j in range(n):
                if map[i][j] == '0':
                    score = [0]
                    self.get_all_hiking_trails(i,j,map,score)
                    ans += score[0]
        return ans
    
    def get_all_hiking_trails(self,x,y,map,trails):
        if map[x][y] == '9':
            trails[0] += 1
            return
        
        pos_x = [-1,0,1, 0]
        pos_y = [0, 1,0,-1]
        
        n = len(pos_x)
        height = int(map[x][y])
        for i in range(n):
            newx = x + pos_x[i]
            newy = y + pos_y[i]
            
            if self.is_valid(newx,newy,map) and map[newx][newy].isdigit() and int(map[newx][newy]) == height + 1:
                self.get_all_hiking_trails(newx,newy,map,trails)
     
solver = day10()
print(solver.solve_part1())
print(solver.solve_part2())