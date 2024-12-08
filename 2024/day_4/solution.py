import regex


class day_4:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        pattern = r"(?=(XMAS|SAMX))"

        result = regex.findall(pattern,text)
        ans = [len(result)]
        
        matrix = [list(line) for line in text.splitlines()]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                self.find_vmatch(i,j,matrix,ans)
                self.find_dmatch(i,j,matrix,ans)
                
        return ans[0]
                
    def find_vmatch(self,i,j,matrix,ans):
        index = 0
        w1 = 'XMAS'
        w2 = 'SAMX'
        
        si = i
        sj = j 
        
        while si < len(matrix) and matrix[si][sj] == w1[index]:
            si += 1
            index += 1
                
            if index == len(w1):
                ans[0] += 1
                break
        
        index = 0
        si = i
        
        while si < len(matrix) and matrix[si][sj] == w2[index]:
            si += 1
            index += 1
                
            if index == len(w2):
                ans[0] += 1
                break
        
    def find_dmatch(self,i,j,matrix,ans):
        index = 0
        w1 = 'XMAS'
        w2 = 'SAMX'
        
        si = i
        sj = j 
        
        while si < len(matrix) and sj < len(matrix[0]) and matrix[si][sj] == w1[index]:
            si += 1
            sj += 1
            index += 1
                
            if index == len(w1):
                ans[0] += 1
                break
        
        index = 0
        si = i
        sj = j
        
        while si < len(matrix) and sj < len(matrix[0]) and matrix[si][sj] == w2[index]:
            si += 1
            sj += 1
            index += 1
                
            if index == len(w2):
                ans[0] += 1
                break
        
        index = 0
        si = i
        sj = j
        
        while si < len(matrix) and sj >= 0 and matrix[si][sj] == w1[index]:
            si += 1
            sj -= 1
            index += 1
                
            if index == len(w2):
                ans[0] += 1
                break
        
        index = 0
        si = i
        sj = j
        
        while si < len(matrix) and sj >= 0 and matrix[si][sj] == w2[index]:
            si += 1
            sj -= 1
            index += 1
                
            if index == len(w2):
                ans[0] += 1
                break
        
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
                    
        matrix = [list(line) for line in text.splitlines()]
        
        ans = 0
        n = len(matrix)
        
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 'A':
                    ans += self.find_MAS(i,j,matrix)
        
        return ans
    
    def find_MAS(self, x,y,matrix):
        pos_x = [-1,-1,1,1]
        pos_y = [-1,1,-1,1]
        MAS_count = 0
        
        for i in range(len(pos_x)):
            mposx = x + pos_x[i]
            mposy = y + pos_y[i]
            sposx = x + (-pos_x[i])
            sposy = y + (-pos_y[i])
            
            if self.is_valid(mposx,mposy,matrix) and self.is_valid(sposx, sposy,matrix) and matrix[mposx][mposy] == 'M' and matrix[sposx][sposy] == 'S':
                MAS_count += 1
                if MAS_count == 2: 
                    return 1
                
        return 0
                
    def is_valid(self, x, y, matrix):
        return 1 if x >= 0 and x < len(matrix) and y >= 0 and y < len(matrix) else 0      
        
solver = day_4()
print(solver.solve_part1())
print(solver.solve_part2())