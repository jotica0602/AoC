class day9:
    def solve_part1(self):
        with open('input.txt','r') as file:
            segment = file.read()
            
        n = len(segment)
        s = []
        id = 0

        # expanding the sequence
        for i in range(n):
            num = int(segment[i])
            
            if i % 2 == 0:
                while num > 0:
                    s.append(str(id))
                    num -= 1
                id += 1
            else:
                while num > 0:
                    s.append('.')
                    num -= 1

        n = len(s)
        index = 0

        for i in range(n):
            if s[i] == '.':
                index = i
                break
            
        for i in range(n-1,-1,-1):
            if s[i] == '.': continue        #savior
            if s[index] == '.':
                s[i],s[index] = '.',s[i]
            else:
                while s[index] != '.':
                    index += 1
                if index >= i + 1:
                    break
                s[i],s[index] = '.',s[i]       

        ans = 0

        #checksum
        for i in range(n):
            if s[i] == '.': continue
            ans += i * int(s[i])

        return ans
    
    def solve_part2(self):
        with open('input.txt','r') as file:
            segment = file.read()
            
        n = len(segment)
        s = []
        id = 0

        # expanding the sequence
        for i in range(n):
            num = int(segment[i])
            
            if i % 2 == 0:
                while num > 0:
                    s.append(str(id))
                    num -= 1
                id += 1
            else:
                while num > 0:
                    s.append('.')
                    num -= 1

        n = len(s)
        moved = set()
        for i in range(n-1,-1,-1):
            if s[i] == '.':
                continue
            else:
                id = s[i]
                if not id in moved:
                    file_block_start, file_block_size = self.capture_block(i,s)
                    condition, free_block_start = self.find_free_space(file_block_size,file_block_start,s) 
                    if condition and not id in moved:
                        self.move_file(free_block_start,file_block_start,s)
                        moved.add(id)
                        
        
        #checksum
        ans = 0
        for i in range(n):
            if s[i] == '.': continue
            ans += i * int(s[i])
            
        return ans
    
    def capture_block(self,index,s):
        start = index
        size = 1
        id = s[index]
        
        while index >= 0 and s[index] == id:
            index -= 1
            size += 1
            
        return (index + 1,size - 1)

    def find_free_space(self,file_block_size,file_block_start,s):
        index = 0
        free_block_size = 0
        reset = True
        
        while index < file_block_start: #and free_block_size != file_block_size:
            if s[index] == '.':
                free_block_size += 1
                if reset:
                    free_block_start = index
                    reset = False
            else:
                reset = True
                free_block_size = 0
            index +=1
        
        return (free_block_size == file_block_size, free_block_start)
    
    def move_file(self, free_block_start, file_block_start, s):
        id = s[file_block_start]
        
        for i in range(free_block_start,file_block_start):
            if s[i] == '.':
                s[i] = id
                s[file_block_start] = '.'
                file_block_start += 1
            else: break
            
            
                
                
            

solver = day9()
print(solver.solve_part1())
print(solver.solve_part2())