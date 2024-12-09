class day9:
    def solve_part1(self):
        with open('input.txt','r') as file:
            segment = file.read()
            
        n = len(segment)
        s = []
        id = 0

        # expanding the sequence
        for i in range(n):
            if i % 2 == 0:
                num = int(segment[i])
                while num > 0:
                    s.append(str(id))
                    num -= 1
                id += 1
            else:
                num = int(segment[i])
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

        for i in range(n):
            if s[i] == '.': continue
            ans += i * int(s[i])

        return ans
    
    def solve_part2(self):
        return -1

solver = day9()
print(solver.solve_part1())
print(solver.solve_part2())