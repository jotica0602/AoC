# import networkx as nx

class day12:
    def solve_part1(self):
        with open('input.txt','r') as file:
            lines = file.read().split()
            
        garden = [list(line) for line in lines]

        n = len(garden)
        groups = {}
        ans = 0
        visited = set()
        for i in range(n):
            for j in range(n):
                if (i,j) not in visited:
                    groups[(i,j)] = [(i,j)]
                    gp = [0]
                    self.group_plants(i,j,garden,[i,j],gp, visited,groups)
                    ans += (len(groups[(i,j)])) * gp[0] 
        return ans
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            lines = file.read().split()
            
        garden = [list(line) for line in lines]

        n = len(garden)
        groups = {}


        ans = 0
        visited = set()
        for i in range(n):
            for j in range(n):
                if (i,j) not in visited:
                    groups[(i,j)] = [(i,j)]
                    gp = [0]
                    self.group_plants(i,j,garden,[i,j],gp,visited,groups)
                
        for key in groups:
            corners = 0
            for x,y in groups[key]:
                corners += self.count_corners(x,y,garden[x][y],key, groups,garden)
                # print(f'{(x,y)}->{corners}')
            ans += corners * len(groups[key])
            
        return int(ans)
    
    def is_in_range(self,x,y,garden):
        return x >= 0 and x < len(garden) and y >= 0 and y < len(garden)

    def group_plants(self,x,y,garden,repr,gp,visited,groups):
        pos = [(-1,0),(0,1),(1,0),(0,-1)]
        visited.add((x,y))
        for i,j in pos:
            if self.is_in_range(x + i,y + j,garden) and garden[x + i][y + j] == garden[x][y]: 
                if (x + i, y + j) not in groups[(repr[0],repr[1])]:
                    groups[(repr[0],repr[1])].append((x + i,y + j))
                    self.group_plants(x + i,y + j, garden, repr, gp, visited,groups)
            else: 
                gp[0] += 1
                
    def count_corners(self,x,y,flower,repr,groups,garden):
        t1 = [(-1,0,0,1,-1,1), (0,1,1,0,1,1), (0,-1,1,0,1,-1), (-1,0,0,-1,-1,-1)]
        t2 = [(0,-1,1,-1), (-1,0,-1,1), (0,1,1,1), (-1,0,-1,-1), (1,0,1,1), (0,-1,-1,-1), (1,0,1,-1), (0,1,-1,1)]
        
        corners = 0
        
        for i,j,k,l,m,n in t1:
            if (not self.is_in_range(x+i,y+j,garden) or garden[x+i][y+j] != flower) and (not self.is_in_range(x+k,y+l,garden) or garden[x+k][y+l] != flower) and (not self.is_in_range(x+m,y+n,garden) or (x+m,y+n) not in groups[repr]):
                corners += 1
        
        for i,j,k,l in t2:
            if self.is_in_range(x+i,y+j,garden) and garden[x+i][y+j] != flower and self.is_in_range(x+k,y+l,garden) and (x+k,y+l) in groups[repr]:
                corners += 0.5
        
        return corners
    
solver = day12()
print(solver.solve_part1())
print(solver.solve_part2())