import regex
class Equation:
    def __init__(self, result, numbers) -> None:
        self.result = result
        self.numbers = numbers
    
    def __str__(self) -> str:
        return f'{self.result} = {self.numbers}'
        
class day7:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read().splitlines()
            
        
        pattern = r'^[\d+]:\s|\d+'
        
        equations = []
        
        for line in text:
            match = regex.findall(pattern,line)
            equation = Equation(int(match[0]),[int(num) for num in match[1:len(match)]])
            equations.append(equation)
            
        ans = [0]      
        for eq in equations:
            self.solve_equation1(eq.result, eq.numbers, ans)
            
        return ans[0]
                       
    def solve_equation1(self, result, numbers, ans):
        ops = ['+', '*']
        self.solve1(result, numbers, numbers[0], ops, 1, ans)
        
    def solve1(self, result, numbers, actual, ops, index, ans):
        if index == len(numbers):
            if actual == result:
                ans[0] += result
                return True
            else:
                return False
        
            
        for op in ops:
            if op == '+' and actual + numbers[index] <= result:
                ok = self.solve1(result,numbers,actual + numbers[index],ops,index + 1, ans)
                if ok: return ok
                
            if op == '*' and actual * numbers[index] <= result:
                ok = self.solve1(result,numbers,actual * numbers[index],ops,index + 1, ans)
                if ok: return ok
            
            # if op == '||' and actual
    
    def solve_equation2(self, result, numbers, ans):
        ops = ['+', '*', '||']
        self.solve2(result, numbers, numbers[0], ops, 1, ans)
        
    def solve2(self, result, numbers, actual, ops, index, ans):
        if index == len(numbers):
            if actual == result:
                ans[0] += result
                return True
            else:
                return False
        
            
        for op in ops:
            if op == '+' and actual + numbers[index] <= result:
                ok = self.solve2(result,numbers,actual + numbers[index],ops,index + 1, ans)
                if ok: return ok
                
            if op == '*' and actual * numbers[index] <= result:
                ok = self.solve2(result,numbers,actual * numbers[index],ops,index + 1, ans)
                if ok: return ok
            
            if op == '||' and self.concat(actual,numbers[index]) <= result:
                ok = self.solve2(result,numbers,self.concat(actual,numbers[index]),ops,index + 1, ans)
                if ok: return ok
            
    def concat(self,x,y):
        return int(str(x)+str(y))
            
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read().splitlines()
            
        
        pattern = r'^[\d+]:\s|\d+'
        
        equations = []
        
        for line in text:
            match = regex.findall(pattern,line)
            equation = Equation(int(match[0]),[int(num) for num in match[1:len(match)]])
            equations.append(equation)
            
        ans = [0]      
        for eq in equations:
            self.solve_equation2(eq.result, eq.numbers, ans)
            
        return ans[0]
        
            
    
solver = day7()
print(solver.solve_part1())
print(solver.solve_part2())