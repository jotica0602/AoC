import regex
import sys

def combo(operand,regs):
    if 0 <= operand <= 3:
        return operand
    if operand == 4:
        return regs['A']
    if operand == 5:
        return regs['B']
    if operand == 6:
        return regs['C']
    else: raise RuntimeError('invalid operand',operand)

def execute(ins,operand,regs,pointer):
    if ins == 0:
        regs['A'] = regs['A'] >> combo(operand,regs)
        # print('a =>> combo')
        pointer[0]+=2
        
    elif ins == 1:
        regs['B'] = regs['B'] ^ operand
        # print('b ^= operand')
        pointer[0]+=2
        
    elif ins == 2:
        regs['B'] = combo(operand,regs) % 8
        # print('b = combo % 8')
        pointer[0]+=2
        
    elif ins == 3:
        if regs['A'] == 0:
            # print('a == 0')
            pointer[0]+=2
        else:
            # print('a != 0 => pointer to 0')
            pointer[0] = operand 
            
    elif ins == 4:
        regs['B'] ^= regs['C']
        # print('b ^= c')
        pointer[0]+=2
        
    elif ins == 5:
        pointer[0] += 2
        # print('combo % 8')
        return str(combo(operand,regs) % 8)
    
    elif ins == 6:
        regs['B'] = regs['A'] >> combo(operand,regs)
        # print('b = a >> combo')
        pointer[0]+=2
        
    else:
        regs['C'] = regs['A'] >> combo(operand,regs)
        # print('c = a >> combo')
        pointer[0]+=2
        
    return ''
        
class day17:
    def solve_part1(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        r = r'\w+\s(\w+):\s(\d+)'
        p = r'Program:\s((\d+,?)+)'
        
        m1 = regex.findall(r,text)
        m2 = regex.findall(p,text)
        
        pointer = [0]
        regs = {r:int(v) for r,v in m1}
        pr = [int(num) for num in m2[0][0].split(',')]
        
        output = []
        while pointer[0] < len(pr):
            output += execute(pr[pointer[0]],pr[pointer[0]+1],regs,pointer)
        
        ans = ','.join(output)
        return ans

    def solve_part2(self):
        with open('input.txt','r') as file:
            text = file.read()
            
        p = r'Program:\s((\d+,?)+)'
        m2 = regex.findall(p,text)
        pr = [int(num) for num in m2[0][0].split(',')]
        
        pr.reverse()
        
        ans = self.find(pr,0)
        return ans
    
    def find(self,program,ans):
        '''
        This is my input so i decided to reverse engineer it: \n
        b = a % 8 \n
        b ^= 3 \n
        c = a >> b \n
        b ^= 5 \n
        a >>= 3 \n
        b ^= c \n
        out b % 8 \n 
        if a == 0 => halt \n
        else pointer = 0 \n
        '''
        
        # Every iteration the program is 
        # right shifting the value of the register A by 3 and passing it to the next iteration 
        # until the value of register A becomes 0.
        # We can also notice that the value of the register B is the remainder of the division
        # of the value in register A by 8, which is the same as the 3 last bits of the register A.
        # We know that if r is the remainder of n divided by 8 then 0 <= r < 8. This means 
        # that left shifting A and adding all the possible values of the register B we can recreate the smallest initial value
        # of the register A
        
        if program == []:
            return ans
        
        for r in range(8):
            a = (ans << 3) ^ r
            b = r
            b ^= 3
            c = a >> b
            b ^= 5
            b ^= c
            if b % 8 == program[0]:
                ok = self.find(program[1:],a)
                if ok: return ok
            
solver = day17()
print(solver.solve_part1())
print(solver.solve_part2())