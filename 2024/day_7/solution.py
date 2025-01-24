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
            
        ans = 0      
        for eq in equations:
            eq:Equation
            if self.solve(eq.result, eq.numbers, eq.numbers[0],1):
                ans += eq.result

        return ans
                       
    def solve(self, result, numbers, actual, index, ops=['+','*']):
        if index == len(numbers):
            if actual == result:
                return True
            else:
                return False

        for op in ops:
            if op == '+' and actual + numbers[index] <= result:
                ok = self.solve(result,numbers,actual + numbers[index],index + 1,ops)
                if ok: return ok
                
            if op == '*' and actual * numbers[index] <= result:
                ok = self.solve(result,numbers,actual * numbers[index],index + 1,ops)
                if ok: return ok
            
            if op == '||' and self.concat(actual,numbers[index]) <= result:
                ok = self.solve(result,numbers,self.concat(actual,numbers[index]),index + 1,ops)
                if ok: return ok
        
        return False
    
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
            
        ans = 0
        for eq in equations:
            eq:Equation
            if self.solve(eq.result,eq.numbers,eq.numbers[0],1,['+','*','||']):
                ans += eq.result
            
        return ans
        
solver = day7()
print(solver.solve_part1())
print(solver.solve_part2())