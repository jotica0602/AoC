import re
import math
        
with open('input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

pattern = r'\w+'
graph = {}

for i in range(2,len(lines)):
    node_values = re.findall(pattern,lines[i])
    u,v,w = node_values
    graph[u] = [v,w]

starters = [k for k in graph.keys() if 'A' in k]
directions = lines[0]
n = len(directions)
l = []

for s in starters:
    current_node = s
    steps = 0
    index = 0
    while 'Z' not in current_node:
        current_node = graph[current_node][0] if directions[index] == 'L' else graph[current_node][1]    
        steps += 1
        index = (index + 1) % n
        
    l.append(steps)

print(math.lcm(*l))