import time
class day15:
    def solve_part1(self):
        with open('map.txt','r') as file:
            text = file.read()
        
        with open('instructions.txt','r') as file:
            instructions = file.read().split('\n')
        
        map = [list(line) for line in text.splitlines()]
        self.print_map(map)
        rx,ry = -1,-1
        
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == '@':
                    rx,ry = i,j
        
        
        for ins in instructions:
            for char in ins:
                self.print_map(map)
                rx,ry = self.move_robot(rx,ry,char,map)
                self.print_map(map)
                
        ans = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'O':
                    ans += 100 * i + j
        return ans
    
    def move_robot(self,rx,ry,ins,map):
        if ins == '^' and map[rx-1][ry] == '.':
           map[rx][ry] = '.'
           rx -= 1
           map[rx][ry] = '@'
        
        elif ins == '^' and map[rx-1][ry] == 'O':
            fx = -1
            
            # find free space
            for i in range(rx-1,0,-1):
                if map[i][ry] == '#' :
                    break
                if map[i][ry] == '.':
                    fx = i
                    break
            if fx >= 0:
                # move boxes
                for i in range(fx,rx):
                    map[i+1][ry] = '.'
                    map[i][ry] = 'O'
                
                # move robot
                map[rx][ry] = '.'
                rx -= 1
                map[rx][ry] = '@'
                
        elif ins == '^' and map[rx-1][ry] == '#':
            pass
        
        elif ins == '>' and map[rx][ry+1] == '.':
            map[rx][ry] = '.'
            ry += 1
            map[rx][ry] = '@'
        
        elif ins == '>' and map[rx][ry+1] == 'O':
            fy = -1
            
            # find free space
            for i in range(ry+1,len(map[0])):
                if map[rx][i] == '#': break
                if map[rx][i] == '.':
                    fy = i
                    break
                
            if fy >= 0:
                # move boxes
                for i in range(fy,ry,-1):
                    map[rx][i-1] = '.'
                    map[rx][i] = 'O'
                
                # move robot
                map[rx][ry] = '.'
                ry += 1
                map[rx][ry] = '@'
        
        elif ins == 'v' and map[rx+1][ry] == '.':
            map[rx][ry] = '.'
            rx += 1
            map[rx][ry] = '@'
        
        elif ins == 'v' and map[rx+1][ry] == 'O':
            fx = -1
            
            # find free space
            for i in range(rx+1,len(map)):
                if map[i][ry] == '#': break
                if map[i][ry] == '.':
                    fx = i
                    break
            if fx >= 0:
                # move boxes
                for i in range(fx,rx,-1):
                    map[i-1][ry] = '.'
                    map[i][ry] = 'O'
                
                # move robot
                map[rx][ry] = '.'
                rx += 1
                map[rx][ry] = '@'
                
        elif ins == 'v' and map[rx+1][ry] == '#':
            pass
        
        elif ins == '<' and map[rx][ry-1] == '.':
            map[rx][ry] = '.'
            ry -= 1
            map[rx][ry] = '@'
            
        elif ins == '<' and map[rx][ry-1] == 'O':
            fy = -1
            
            # find free space
            for i in range(ry-1,0,-1):
                if map[rx][i] == '#': break
                if map[rx][i] == '.':
                    fy = i
                    break
                
            if fy >= 0:
                # move boxes
                for i in range(fy,ry):
                    map[rx][i+1] = '.'
                    map[rx][i] = 'O'
                
                # move robot
                map[rx][ry] = '.'
                ry -= 1
                map[rx][ry] = '@'
        
        elif ins == '<' and map[rx][ry-1] == '#':
            pass
        
        return rx,ry
        
    def print_map(self,map):
        time.sleep(0.5)
        print("\033c", end="")  
        for i in range(len(map)):
            for j in range(len(map[i])):
                print(map[i][j],sep='',end='')
            print()
 
    def solve_part2(self):
        with open('map.txt','r') as file:
            text = file.read()
    
        with open('instructions.txt','r') as file:
            instructions = file.read().split('\n')
        
        replacements = [('#','##'),('O','OO'),('.','..'),('@','@.')]
        
        for old,new in replacements:
            text =text.replace(old,new)
        
        map = [list(line) for line in text.splitlines()]
        self.print_map(map)
        # exit()
        rx,ry = -1,-1
        
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == '@':
                    rx,ry = i,j
        
        c = 0
        for ins in instructions:
            for char in ins:
                self.print_map(map)
                rx,ry = self.move_robot(rx,ry,char,map)
                self.print_map(map)
                # if c == 6:
                #     exit()
                
        ans = 0
        for i in range(len(map)):
            for j in range(len(map[0])):
                if map[i][j] == 'O':
                    ans += 100 * i + j
        return ans
    
solver = day15()
# print(solver.solve_part1())
print(solver.solve_part2())