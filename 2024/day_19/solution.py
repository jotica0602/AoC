import re
class day19():
    def solve_part1(self):
        with open('input1.txt') as available_patterns:
            available = available_patterns.read()
        with open('input2.txt') as d:
            d = d.read()
        
        p = r'\w+'
        patterns = re.findall(p,available)
        designs = re.findall(p,d)
        ans = 0
        processed = 0
        
        for design in designs:
            result = self.is_possible_p1(design,patterns)
            if result: 
                ans += result   
                print(f'{design} possible')
            
            else: print(f'{design} impossible')
            processed += 1
            
        print(f'processed: {processed}')
        return ans
    
    def is_possible_p1(self,design,patterns):
        if design == '':
            return 1
        
        for pattern in patterns:
            if design.startswith(pattern):
                ok = self.is_possible_p1(design[len(pattern):],patterns)
                if ok: return 1
            
        return 0             
            
    def solve_part2(self):
        with open('input1.txt') as available_patterns:
            available = available_patterns.read()
        with open('input2.txt') as d:
            d = d.read()
        
        p = r'\w+'
        patterns = re.findall(p,available)
        designs = re.findall(p,d)
        ans = 0
        memo = {}
                
        for design in designs:
            ans += self.is_possible_p2(design,patterns,memo)   
            # print(f'{design} possible')
            # processed += 1
            
        # print(f'processed: {processed}')
        return ans
    
    def is_possible_p2(self,design,patterns,memo):
        if design == '':
            return 1
        
        if design in memo:
            return memo[design]
        
        ok = 0
        for pattern in patterns:
            if design.startswith(pattern):
                ok += self.is_possible_p2(design[len(pattern):],patterns,memo)
        
        memo[design] = ok
        return ok            
    
solver = day19()
print(solver.solve_part1())
print(solver.solve_part2())