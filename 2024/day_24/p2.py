import re
from graphviz import Digraph
class LOP:
    def __init__(self,left,operation,right,result) -> None:
        self.left = left
        self.right = right
        self.operation = operation
        self.result = result
        
    def __str__(self) -> str:
        return f'{self.left} {self.operation} {self.right} = {self.result}'

G = Digraph()
wires = {}
aliases = {}

with open('input.txt','r') as file:
    input = file.read()

p1 = r'(\w+):\s\d+'
p2 = r'(\w+)\s(\w+)\s(\w+)\s->\s(\w+)'

ops = []
wires = re.findall(p1,input)

for wire in wires:
    G.node(wire)

print(G)
gates = re.findall(p2,input)

i = 0
for gate in gates:
    left,op,right,result = gate
    op = op + str(i)
    G.edge(left,op)
    G.edge(right,op)
    G.edge(op,result)
    i+=1


G.view()
print(str.join(',',sorted(['z10','mkk','z14','qbw','cvp','wjb','wcb','z34'])))