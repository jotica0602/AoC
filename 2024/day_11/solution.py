import regex
class day11:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        pattern = '\d+'
        numbers = regex.findall(pattern,text)
        new_numbers = []
        
        blinks = 0
        while blinks < 25:
            for i in range(len(numbers)):
                if int(numbers[i]) == 0:
                    new_numbers.append('1')
                elif len(numbers[i]) % 2 == 0:
                    n = len(numbers[i])
                    new_numbers.append(str(int(numbers[i][:n//2])))
                    new_numbers.append(str(int(numbers[i][n//2: n])))
                else:
                    new_numbers.append(str(int(numbers[i]) * 2024))
            numbers = new_numbers
            new_numbers = []
            blinks += 1
        ans = len(numbers)
        
        return ans
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        pattern = '\d+'
        numbers = regex.findall(pattern,text)
        cache = {}
        ans = 0
        for i in range(len(numbers)):
            if numbers[i] in cache:
                ans += cache[numbers[i]]
            else:
                ans += self.get_blinks(75,int(numbers[i]),cache)
        
        return ans
    
    def get_blinks(self,blinks,number,cache):
        n = len(str(number))
        
        if (number,blinks) in cache:
            return cache[(number,blinks)]
        elif blinks == 0:
            return 1
        elif number == 0:
            result =  self.get_blinks(blinks - 1, 1,cache) 
            cache[(number,blinks)] = result
            return result
        elif n % 2 == 0:
            result = self.get_blinks(blinks - 1, int(str(number)[:n//2]),cache) + self.get_blinks(blinks - 1, int(str(number)[n//2:n]),cache)
            cache[(number,blinks)] = result
            return result
        else:
            result = self.get_blinks(blinks - 1, number * 2024,cache)
            cache[(number,blinks)] = result
            return result
            
         
solver = day11()
print(solver.solve_part1())
print(solver.solve_part2())