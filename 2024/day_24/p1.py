import re
class LOP:
    def __init__(self,left,operation,right,result,wires) -> None:
        self.left = left
        self.right = right
        self.operation = operation
        self.result = result
        
    def operate(self):
        match self.operation:
            case 'AND':
                wires[self.result] = wires[self.left] & wires[self.right]
            case 'OR':
                wires[self.result] = wires[self.left] | wires[self.right]
            case 'XOR':
                wires[self.result] = wires[self.left] ^ wires[self.right]
            
    def __str__(self) -> str:
        return f'{self.left} {self.operation} {self.right} = {wires[self.result]}'

wires = {}

with open('input.txt','r') as file:
    input = file.read()

p1 = r'(\w+):\s(\d+)'

for m in re.findall(p1,input):
    wire,value = m
    wires[wire] = int(value)

x = [str(wires[key]) for key in sorted([key for key in wires.keys() if key.startswith('x')],reverse=True)]
y = [str(wires[key]) for key in sorted([key for key in wires.keys() if key.startswith('y')],reverse=True)]

x = int(str.join('',x),base=2)
y = int(str.join('',y),base=2)

print(' ' + str(x) + '\n+' + str(y) + '\n' + '_' * (max(len(str(x)),len(str(y))) + 1) + '\n ' + str(x+y))
p2 = r'(\w+)\s(\w+)\s(\w+)\s->\s(\w+)'


ops = []
for m in re.findall(p2,input):
    left,op,right,result = m
    ops.append(LOP(left,op,right,result,wires))


def solve_ops(operations:list[LOP],operation:LOP,wires:dict):
    if not operation.left in wires or not operation.right in wires:
        ts = [op for op in operations if op.result == operation.left or op.result == operation.right]
        for op in ts:
            solve_ops(operations,op,wires)
    operation.operate()
        
for op in ops:
    solve_ops(ops,op,wires)
    
res = sorted([key for key in wires.keys() if key.startswith('z')],reverse=True)
ans = ''

for key in res:
    ans += str(wires[key])
    
print(' ' + str(int(ans,base=2)))

