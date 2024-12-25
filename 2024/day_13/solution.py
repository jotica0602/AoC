import regex

class day13:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        pattern = r'\d+'
        m = regex.findall(pattern,text)
        
        ans = 0
        for i in range(0,len(m),6):
            a1,a2,b1,b2,c1,c2 = int(m[i]),int(m[i+1]),int(m[i+2]),int(m[i+3]),int(m[i+4]),int(m[i+5])
            ans += self.get_cost(a1,a2,b1,b2,c1,c2,3,1)
        
        return int(ans)
        
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
        
        pattern = r'\d+'
        m = regex.findall(pattern,text)
        
        ans = 0
        for i in range(0,len(m),6):
            a1,a2,b1,b2,c1,c2 = int(m[i]),int(m[i+1]),int(m[i+2]),int(m[i+3]),int(m[i+4])+10000000000000,int(m[i+5])+10000000000000
            ans += self.get_cost(a1,a2,b1,b2,c1,c2,3,1)
        
        return int(ans)
    
    def get_cost(self,a1,a2,b1,b2,c1,c2,cA,cB):
        x = (c2*b1 - c1*b2)/(a2*b1-a1*b2)
        y = (a1*c2 - a2*c1)/(a1*b2-a2*b1)
        
        if x % 1 == 0 and y % 1 == 0:
            return cA*x + cB*y
        else: return 0
        
    
solver = day13()
print(solver.solve_part1())
print(solver.solve_part2())